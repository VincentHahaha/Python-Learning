print("\n快輸入五個數字 !! (每輸入一個記得Enter)\n")

n1=int(input("來第一個 :　"))
n2=int(input("來第二個 :　"))
n3=int(input("來第三個 :　"))
n4=int(input("來第四個 :　"))
n5=int(input("來第五個 :　"))

l=[n1,n2,n3,n4,n5]
x=max(l)

s=n1+n2+n3+n4+n5

x=str(x)
s=str(s)

print("\n各 位 觀 眾 ! \n\n總和是 : ",s,"    猛吧 ?!")
print("最大尾的是 : ",x,"    猜對了?!\n")

print("謝謝,可以休息啦~~")