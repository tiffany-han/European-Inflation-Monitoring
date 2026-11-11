
import requests
import pandas as pd
from sqlalchemy import create_engine

url= "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_minr?format=JSON"

sql_password= " "

params = {
    "lang": "EN", #language
    "unit": "I25", #Unit of measure
    "coicop18": "TOTAL", #Classification of individual consumption by purpose
}

response = requests.get(url ,params= params)

data = response.json()

country_name= data["dimension"]["geo"]["category"]["label"]
country_code= data["dimension"]["geo"]["category"]["index"]


country_df= pd.DataFrame({"country_code":list(country_code.keys()),
                          "country_name":list(country_name.values())})

# country_df.to_csv("country_reference.csv", index=False, encoding="utf-8-sig")


#add a columns to identify EU member states
eu_members = [
    'AT', 'BE', 'BG', 'HR', 'CY',
    'CZ', 'DK', 'EE', 'FI', 'FR',
    'DE', 'EL', 'HU', 'IE', 'IT',
    'LV', 'LT', 'LU', 'MT', 'NL',
    'PL', 'PT', 'RO', 'SK', 'SI',
    'ES', 'SE'
]

country_df['is_eu_member'] = (
    country_df['country_code'].isin(eu_members)
)

print(country_df.head())
print(country_df["is_eu_member"].value_counts())

#wirte the country reference to the database
engine= create_engine("mysql+pymysql://root:"+sql_password+"@localhost:3306/eurostat")
country_df.to_sql(name="country_reference", con=engine, if_exists="replace", index=False)

