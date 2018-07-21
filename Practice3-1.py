# 程式包裝
# 1. 把 99 乘法表包裝成函式，可做 n1xn2 乘法 
# 2. 把四則運算機包裝成函式
# 3. 將以上函式包裝在自己的模組和封包中，並且在主程式成功使用

import Prac3.multiple as m
import Prac3.calculate as c

while True:

    print("\n1. 四則運算機\n2. n1 x n2 乘法表 \n")
    choice=input("輸入 1 或 2 選擇你要執行的項目 : ")

    if choice=="1" :
    
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

                c.Cal(n1,n2,op)
                break
            
    elif choice=="2" :
        x=int(input("\nEnter n1 : "))
        y=int(input("Enter n2 : "))

        if x<y:
            print("\n")
            m.list(x,y)
            print("\n")
        elif x>y:
            print("\n")
            m.list(y,x)
            print("\n")
        else:
            print("\n",x,"x",y,"=",x*y,"\n")
    
    else:
        print("\n賣鬧 ! \n")
        continue

    ans=input("Do You Wanna Play Again ? (y/n) : ")

    if ans=="Y" or ans=="y" :
        print("\n")
        continue
    else :
        print("\nBye !")
        break