
import requests
import pandas as pd

url= "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_minr?format=JSON"


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

country_df.to_csv("country_reference.csv", index=False, encoding="utf-8-sig")


