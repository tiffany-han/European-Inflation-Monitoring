
import requests
import pandas as pd

url= "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_minr?format=JSON"


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

unit_df.to_csv("unit_reference.csv", index=False, encoding="utf-8-sig") 

