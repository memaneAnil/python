import threading

def Thread1(No):
    for iCnt in range(1,No+1,1):
        print(iCnt)
            


def Thread2(No):
    print("______________________")
    for iCnt in range(No,0,-1):
        print(iCnt)
            
    



def main():

    Number=50

    t1=threading.Thread(target=Thread1,args=(Number,))
    t2=threading.Thread(target=Thread2,args=(Number,))

    t1.start()
    t1.join()
   
    t2.start()
    t2.join()
    

if __name__=="__main__":
    main()