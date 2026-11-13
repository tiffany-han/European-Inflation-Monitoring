
import requests
import pandas as pd
from sqlalchemy import create_engine

url= "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_minr?format=JSON"

sql_password= "123456789"

params = {
    "lang": "EN", #language
    "coicop18": "TOTAL"
}

response = requests.get(url ,params= params)

data = response.json()

unit= data["dimension"]["unit"]["category"]["label"]
unit_code= data["dimension"]["unit"]["category"]["index"]

unit_df= pd.DataFrame({"unit_code":list(unit_code.keys()),
                          "unit":list(unit.values())})

# unit_df.to_csv("unit_reference.csv", index=False, encoding="utf-8-sig") 

#wirte the unit reference to the database
engine= create_engine("mysql+pymysql://root:"+sql_password+"@localhost:3306/eurostat")
unit_df.to_sql(name="unit_reference", con=engine, if_exists="replace", index=False)
