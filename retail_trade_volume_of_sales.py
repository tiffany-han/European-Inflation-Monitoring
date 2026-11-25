# %% extract data

import requests
from pyjstat import pyjstat
from sqlalchemy import create_engine

url= "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/sts_trtu_m?format=JSON"


params = {
    "lang": "EN", #language
    "unit": ["PCH_SM","I21"],
    "indic_bt": "VOL_SLS",
    "nace_r2": "G47_FOOD", #specify the desired categories
    "s_adj":"CA",
    "geo": ["NL","BE"], #"EU27_2020" #Classification of vidual consumption by purpose
    "sinceTimePeriod": "2026-10",
    "untilTimePeriod": "2026-10"
}

info = requests.get(url ,params= params)

if info.status_code == 200:
    print("Data extraction successfully")
else:
    print("Date extraction failed，Error message:",info.status_code)
    
data = info.json()

dataset= pyjstat.Dataset.read(info.text)

df = dataset.write("dataframe")

#rename the columns
df= df.rename(columns= {
    "Statistical classification of economic activities in the European Community (NACE Rev. 2)":"classification of economic activities",
    "Geopolitical entity (reporting)":"country_name"})

print(df)
# df.to_csv("retail_trade_volume_of_sales.csv", mode="w", index=False, encoding="utf-8-sig") 

#wirte the data to the database
sql_password= " "
engine= create_engine("mysql+pymysql://root:"+sql_password+"@localhost:3306/eurostat")
#use "replace" for the initial load; use "append" for subsequent updates to avoid overwriting existing data
df.to_sql(name="retail_trade_volume_of_sales", con=engine, if_exists="replace", index=False)

