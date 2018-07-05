# 四則運算

while True :
   
    print('\n這是小學生計算機, 運算式請輸入 "+,-,*,/" \n')
    print("輸入格式 : 3 * 5  (全部輸入完請按 Enter ) \n")
    try:
        n1,op,n2=input().split() 
    except ValueError:
        print("\n忘記空格了齁！ 重來 OK ?!\n")
        continue
        
    

    n1=int(n1)
    n2=int(n2)


    print("= ",end="")


    if op =="+":
        print(n1+n2)
            

    elif op =="-":
        print(n1-n2)
            

    elif op =="*":
        print(n1*n2)
            

    elif op =="/":
        print(n1/n2)
            

    else :
        print("What the hell ?")

    print("\n")

    

        
