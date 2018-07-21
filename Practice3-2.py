# 從官網資訊學習使用系統內建的模組 random 產生 1~100 間的亂數


import random

# n = random.randint(1,100)

# 呈現 1~100  10x10 亂數矩陣

x=random.sample(range(1,101),k=100)
a=1
while a<=100:
    if a%10==0:
        print(x[a-1])
        a+=1
    else:
        print(x[a-1],end="\t")
        a+=1

