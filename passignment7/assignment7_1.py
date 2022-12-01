import threading

def Even(No):
    for iCnt in range(1,No+1,1):
        if(iCnt%2==0):
            print("Even number",iCnt)


def Odd(No):
    for iCnt in range(1,No+1,2):
        #if(iCnt%2!=0):
            print("Odd number",iCnt)




def main():

    Number=20

    t1=threading.Thread(target=Even,args=(Number,))
    t2=threading.Thread(target=Odd,args=(Number,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    

if __name__=="__main__":
    main()