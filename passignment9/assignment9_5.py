import os.path

def Frequency(filename,str):
    iCnt=0
    fd=open(filename,'r')
    for line in fd:
        arr=line.split()
        for word in arr:
            if(word==str):
                iCnt=iCnt+1
    return iCnt
   
def main():
    print("Enter first file name")
    fname1=input()
    print("Enter the string")
    fname2=input()
    iRet=Frequency(fname1,fname2)
    print("frequency of {} in file {} is {} ".format(fname2,fname1,iRet))
    

if __name__=="__main__":
    main()
