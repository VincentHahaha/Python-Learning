# 使用者輸入一個正整數，算整數平方根

while True:

    print("\n我要來算平方根, you know.")
    n=int(input("請輸入一個正整數 : "))
    x=1

    while x**2 <= n:
        
        if x**2 == n:
            print("\n",n,"的平方根 = " ,x)
            break

        else :
            x+=1
    if x**2>n :
        print("\nSorry 我只有國中智商...")
        print("輸入個我會算的 QAQ\n")
        continue
    
    else:
        w=input("\n還要再看我表演一次嗎？ y or n  :")

    if w=="y" :

        continue

    else:
        print("\nBye !")

        break

