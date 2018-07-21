
def list(n1,n2) :
    
    for w in range(n1,n2+1) :

        for n in range(n1,n2):
            
            if n*w <10 :
                print(n,"x",w,"= ",n*w,end="     ")

            else:
                print(n,"x",w,"=",n*w,end="     ")

        if w==1 and n2==9 :

            print(9,"x",w,"=  ",9*w)
        else:
            
            print(n2,"x",w,"= ",n2*w)
        
    return

