print("\n快輸入五個數字 !! (每輸入一個記得Enter)\n")

# n1=int(input("來第一個 :　"))
# n2=int(input("來第二個 :　"))
# n3=int(input("來第三個 :　"))
# n4=int(input("來第四個 :　"))
# n5=int(input("來第五個 :　"))

n1=input("來第一個 :　")
n2=input("來第二個 :　")
n3=input("來第三個 :　")
n4=input("來第四個 :　")
n5=input("來第五個 :　")


list_n=[n1,n2,n3,n4,n5]

if n1 and n2 and n3 and n4 and n5:
    
    n1,n2,n3,n4,n5=(int(x) for x in list_n)
    
   

    x=max(list_n)
    s=n1+n2+n3+n4+n5

    x=str(x)
    s=str(s)

    print("\n各 位 觀 眾 ! \n\n總和是 : ",s,"    猛吧 ?!")
    print("最大尾的是 : ",x,"    猜對了?!\n")

    print("謝謝,可以休息啦~~")

else:
    print("\n你少輸入一個,耍我阿 ?!")

    # print(len(list_n))