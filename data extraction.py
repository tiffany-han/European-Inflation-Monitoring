import requests
import pandas as pd
import time
# from pyjstat import pyjstat


#設定query參數
countries= ["NL","ES"]
sinceTimePeriod= ["2026-07"]
untilTimePeriod= ["2026-09"]
categories= ["TOTAL","CP01"]

#建立只有欄位的excel檔
df= pd.DataFrame(columns=["country_code","country_name","categories","period","value"])
df.to_csv("eurostat_hicp.csv",  index=False, encoding="utf-8-sig")

for geo in countries:
    for coicop18 in categories:
        url= "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hicp_minr?format=JSON"
    
        params = {
            "lang": "EN", #language
        #     "freq": "M",
            "unit": "I25", #Unit of measure
            "coicop18": coicop18, #Classification of individual consumption by purpose
            "geo": geo,
            "sinceTimePeriod": sinceTimePeriod,
            "untilTimePeriod": untilTimePeriod
        }
        
        info = requests.get(url ,params= params)
        
        if info.status_code == 200:
            print(geo,'資料擷取成功')
        else:
            print(geo,'失敗，錯誤訊息:',info.status_code)
            
        data = info.json()
        # print(data["dimension"].keys()) #確認有什麼key
        
        #period
        lst_time = list()
        for j in data["dimension"]["time"]["category"]["index"]: 
            lst_time.append(j)
        
        #HICP values
        lst_data = list()
        for i in data["value"].values(): #values取得對應數值
            lst_data.append(i)
            
        country_name= list(data["dimension"]["geo"]["category"]["label"].values())[0]
        print(geo,country_name,coicop18,lst_time,lst_data) #check

        df= pd.DataFrame({"country_code":geo,"country_name":country_name,
                          "categories":coicop18,"period":lst_time,"value":lst_data})
        print(df)
        df.to_csv("eurostat_hicp.csv", mode="a", index=False, encoding="utf-8-sig", header=False) #header=false是只取列資料不取欄位
        time.sleep(2) #設定間格時間以免被鎖住
    time.sleep(2)
# country_code=list(data["dimension"]["geo"]["category"]["index"].keys())[0]
# print(country_code)

# df.insert(0,"country_code",country_code)
# print(df)
# df.to_csv("eurostat_hicp.csv", mode="a", index=False, encoding="utf-8-sig")
    


# dataset= pyjstat.Dataset.read(data.text)
# df = dataset.write('dataframe')

# print(df.head())
# print(df.columns)
