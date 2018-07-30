# 1. 使用台北公開資料的 [台北市台北旅遊網-景點資料]
# 2. 使用者可以用捷運站名稱蒐尋景點
# 3. 將對應到的景點資訊儲存在檔案中

import urllib.request as request
import json

with request.urlopen("http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=36847f3f-deff-4183-a5bb-800737591de5") as response:
    data=json.load(response)

while True:
    key=input("輸入你所在的捷運站吧！ ：")
    list=data["result"]["results"]
    print("\n")
    n=0

    with open("place.txt","a",encoding="utf-8") as file:
    
        file.write("\nFor 捷運")
        file.write(key)
        file.write("\n\n")
        for place in list:
            #try:
                if key==place["MRT"] :
            
                    print(place["stitle"])
                    print(place["MEMO_TIME"],"\n")
                    
                    file.write(place["stitle"]+"\n")
                    file.write(place["MEMO_TIME"])
                    file.write("\n\n")
                    
                    n+=1

            # except TypeError:
            #     continue
        if n<=0:
            print("請輸入完整的站名！\n")
            file.write("沒這鳥地方...\n")
            continue
        else:
            print("以上是",key,"捷運站附近景點！")
            break