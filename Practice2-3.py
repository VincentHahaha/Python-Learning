# 輸出九九乘法表

print("Ladies & Gentleman !")
print("來看我一次變出九九乘法表囉！")
print("倒數五秒~\n")

import threading
import time

def fun_timer():
    
    print("秒")
    global timer
    timer = threading.Timer(1, fun_timer)
    timer.start()

print("秒")

timer = threading.Timer(1, fun_timer)
timer.start()

time.sleep(5)
timer.cancel()


for w in range(1,10) :

    for n in range(1,9):
        
        if n*w <10 :
            print(n,"x",w,"= ",n*w,end="     ")

        else:
            print(n,"x",w,"=",n*w,end="     ")

    if w==1:
        print(9,"x",w,"= ",9*w)
    else:
        print(9,"x",w,"=",9*w)

   
    