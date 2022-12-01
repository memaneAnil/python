import threading

def Evenlist(arr):
    add=0
    for no in arr:
        print(no)
        if(no%2==0):
            add=add+no

    print("Addition of even no :",add)

def Oddlist(arr):
    add=0
    for no in arr:
        print(no)
        if(no%2!=0):
            add=add+no

    print("Addition of odd no :",add)

def main():
    iArr=[]

    print("Enter the size")
    iSize=int(input())

    for iCnt in range(0,iSize,1):
        number=int(input())
        iArr.append(number)

    print(iArr)

    t1=threading.Thread(target=Evenlist,args=[iArr,])
    t2=threading.Thread(target=Oddlist,args=[iArr,])
 
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    

if __name__=="__main__":
    main()