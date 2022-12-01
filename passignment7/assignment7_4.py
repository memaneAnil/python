import threading

def small(str):
    print("thread name: ",threading.current_thread().name)
    print("thread id ",threading.get_ident())
    Cnt=0
    for ch in str:
        
        if(ch>='a' and ch<='z'):
            
            Cnt=Cnt+1
            
    print("--------------------Number of small char :",Cnt)

def capital(str):
    print("thread name: ",threading.current_thread().name)
    print("thread id ",threading.get_ident())
    Cnt=0
    for ch in str:
        
        if(ch>='A' and ch<='Z'):
            
            Cnt=Cnt+1

           
    print("---------------------Number of Capital char :",Cnt)

def digit(str):
    print("thread name: ",threading.current_thread().name)
    print("thread id ",threading.get_ident())
    Cnt=0
    for ch in str:
        
        if(ch>='0' and ch<='9'):
            
            Cnt=Cnt+1

          
    print("---------------------Number of digit :",Cnt)


def main():
    print("Enter the String")
    Name=input()
    t1=threading.Thread(target=small,args=(Name,))
    t2=threading.Thread(target=capital,args=(Name,))
    t3=threading.Thread(target=digit,args=(Name,))
    t1.start()
    t2.start()
    t3.start()

    print("thread name: ",threading.current_thread().name)
    print("thread id ",threading.get_ident())
    
    t1.join()
    t2.join()
    t3.join()
    

    

if __name__=="__main__":
    main()