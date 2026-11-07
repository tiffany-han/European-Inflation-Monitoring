
import requests
import pandas as pd

url= "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_minr?format=JSON"


params = {
    "lang": "EN", #language
    "unit": "I25", #Unit of measure
    "geo": "NL"
}

response = requests.get(url ,params= params)

data = response.json()

category= data["dimension"]["coicop18"]["category"]["label"]
category_code= data["dimension"]["coicop18"]["category"]["index"]

category_df= pd.DataFrame({"category_code":list(category_code.keys()),
                          "category":list(category.values())})

#select the required category columns
category_df= category_df[category_df["category_code"].str.match(r"^(TOTAL|NRG|ELC_GAS|FUEL|SERV|TOT_X_NRG|TOT_X_FUEL|IGD_NNRG|CP\d{2})$")]

category_df.to_csv("category_reference.csv", index=False, encoding="utf-8-sig") 

