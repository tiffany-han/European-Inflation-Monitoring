# %% create an Excel

import pandas as pd

#create an Excel with column headers only
df= pd.DataFrame(columns=["Country_code","Country_name","Unit of measure",
                          "Category_code","Category","Period","Year","Month","Value"])
df.to_csv("eurostat_hicp_test.csv",  index=False, encoding="utf-8-sig")


# %% extract data

import requests
from pyjstat import pyjstat
from sqlalchemy import create_engine

url= "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_minr?format=JSON"

country_csv= pd.read_csv("country_reference.csv")
countries= country_csv["country_code"].tolist()

category_csv= pd.read_csv("category_reference.csv")
categories= category_csv["category_code"].tolist()

# geo= countries 
geo= ["EU27_2020"] #specify the desired range
sinceTimePeriod= ["2025-01"]
untilTimePeriod= ["2026-09"]
# coicop18= categories 
coicop18= ["TOTAL"] #specify the desired range
# unit= ["I25","RCH_M","RCH_A"]
unit= ["I25"] #specify the desired range
sql_password= " "

params = {
    "lang": "EN", #language
    "unit": unit, #Unit of measure
    "coicop18": coicop18, #Classification of individual consumption by purpose
    "geo": geo,
    "sinceTimePeriod": sinceTimePeriod,
    "untilTimePeriod": untilTimePeriod
}

info = requests.get(url ,params= params)

if info.status_code == 200:
    print("Data extraction successfully")
else:
    print("Date extraction failed，Error message:",info.status_code)
    
data = info.json()


dataset= pyjstat.Dataset.read(info.text)
df = dataset.write("dataframe")

units= list(data["dimension"]["unit"]["category"]["index"].keys())
geo_codes= list(data["dimension"]["geo"]["category"]["index"].keys())
coicop_codes = list(data["dimension"]["coicop18"]["category"]["index"].keys())
time_ = list(data["dimension"]["time"]["category"]["index"].keys())

#add columns
unit_list = []
categories_list = []
countries_list = []
for unit_ in units:
    for category_code in coicop_codes:
        for country_code in geo_codes:
            for time in time_:
                unit_list.append(unit_)
                categories_list.append(category_code)
                countries_list.append(country_code)
            
df["unit"]=unit_list
df["country_code"]=countries_list
df["category_code"]=categories_list


#split the period column into year and month columns
df[["Year","Month"]]= (df["Time"].str.split("-", expand=True).astype(int))

#rename the columns
df= df.rename(columns= {
    "Classification of individual consumption by purpose (COICOP) - 2018":"category",
    "Geopolitical entity (reporting)":"country_name"})

#reorder the columns
df= df[["country_code","country_name",
       "Unit of measure","category_code",
       "category",
       "Time","Year","Month","value"]]


#wirte the data to the database
engine= create_engine("mysql+pymysql://root:"+sql_password+"@localhost:3306/eurostat")
df.to_sql(name="hicp_data", con=engine, if_exists="append", index=False)

#write the data to csv
# df.to_csv("eurostat_hicp.csv", mode="a", index=False, encoding="utf-8-sig", header=False) 
