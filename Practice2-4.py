# 質數偵測

print("\n我要來幫你檢查是不是質數了, you know.")
n=int(input("請輸入一個正整數 : "))
print("\n",n,"的因數有 : ",end="")
const=0

for x in range(1,n+1) :

    if n%x ==0 :

        print(x,",",end=" ")
        const+=1


if const >=3 :

    print("\n\n除了 1 和",n,"以外還有其他因數")
    print("\n所以",n,"不是質數 ~")

else:
    print("\n\n唉呦, 看來",n,"是質數喔 ~")

