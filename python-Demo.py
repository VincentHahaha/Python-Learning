import urllib.request as request
import ssl
import bs4

# import sys   
# sys.setrecursionlimit(1000000)

def getData(src):

    context=ssl._create_unverified_context()
    req=request.Request(src, headers={     
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    })

    with request.urlopen(req,context=context) as response:
        data=response.read().decode("utf-8")
    
    root=bs4.BeautifulSoup(data,"html.parser")
    td_tag=root.find_all("td")
    totalList=[]
    for t in td_tag:
        totalList.append(t.string)
    
    x=2
    industryList2018=[]
    industryList2017=[]
    industryList2016=[]
    countryList2018=[]
    countryList2017=[]
    countryList2016=[]

    while x<len(totalList) :
        if "2018" in totalList[x]:
            industryList2018.append(totalList[x+2])
            countryList2018.append(totalList[x+1])
            x+=6
        elif "2017" in totalList[x]:
            industryList2017.append(totalList[x+2])
            countryList2017.append(totalList[x+1])
            x+=6
        elif "2016" in totalList[x]:
            industryList2016.append(totalList[x+2])
            countryList2016.append(totalList[x+1])
            x+=6
        else:
            x+=6
    cLtotal=countryList2018+countryList2017+countryList2016
    return {
        "iL2018":industryList2018,
        "iL2017":industryList2017,
        "iL2016":industryList2016,
        "cL2018":countryList2018,
        "cL2017":countryList2017,
        "cL2016":countryList2016,
        "cLtotal":cLtotal
    }

def clear_account(lists):
#去除重複的值
	wokey={}
	wokey=wokey.fromkeys(lists)
 
	word_1=list(wokey.keys())
#統計元素的出現次數，存入字典
	for i in word_1:
		wokey[i]=lists.count(i)
	return wokey

def sort_1(wokey):
    wokey_1={}
    wokey_1=sorted(wokey.items(), key=lambda d:d[1], reverse=True)

    # sum=0
    # x=len(wokey_1)
    # for w in wokey_1[3:x+1]:
    #     sum=sum+w[1]
    wokey_1=wokey_1[0:3] # +[('Others',sum)]
    wokey_1=dict(wokey_1)
    return wokey_1


    
# Demo_main

src="https://www.cbinsights.com/research-unicorn-companies"
data=getData(src)
a=sort_1(clear_account(data["iL2018"]))
b=sort_1(clear_account(data["iL2017"]))
c=sort_1(clear_account(data["iL2016"]))


# import plotly.plotly as py
# import plotly.graph_objs as go

# def goBar(set, year):
#     labels=[]
#     values=[]

#     for name in set:
#         labels.append(name)
#         values.append(set[name])
#     data = [go.Bar(
#                 x=labels,
#                 y=values
#         )]

#     py.plot(data, filename=year+' Industry distribution',auto_open=True)


# goBar(a,"2018")
# goBar(b,"2017")
# goBar(c,"2016")

# 產業類別

def getLV(set):
    labels=[]
    values=[]

    for name in set:
        labels.append(name)
        values.append(set[name])
    print(labels)
    print(values)

getLV(a)
getLV(b)
getLV(c)

# 國家分佈

print(len(data["cLtotal"]))
wokey=clear_account(data["cLtotal"])

wokey_1={}
wokey_1=sorted(wokey.items(), key=lambda d:d[1], reverse=True)

sum=0
x=len(wokey_1)
for w in wokey_1[3:x+1]:
    sum=sum+w[1]
wokey_1=wokey_1[0:3]+[('Others',sum)]
wokey_1=dict(wokey_1)

getLV(wokey_1)