import threading

def Evenfactor(No):
    add=0
    for iCnt in range(2,int(No/2+1),2):
        if(No%iCnt==0):
            add=add+iCnt
    print("Addition of Even factor is :",add)

def Oddfactor(No):
    add=0
    for iCnt in range(1,int(No/2+1),2):
        if(No%iCnt==0):
            add=add+iCnt
            
    print("Addition of odd factor is :",add)
        



def main():

    print("Enter the number")
    Number=int(input())

    t1=threading.Thread(target=Evenfactor,args=(Number,))
    t2=threading.Thread(target=Oddfactor,args=(Number,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()    
    print("exit from main")

if __name__=="__main__":
    main()