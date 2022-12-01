import os.path
import filecmp
from sys import *
def Compare_File(file1,file2):
    fd1=open(file1,'r')
    fd2=open(file2,'r')
    for line1 in fd1:
        for line2 in fd2:
            if(line1==line2):
                return True
    
    

def main():
    if(len(argv)!=3):
        print("Insufficient argument")
        exit()
    else:
        bRet=Compare_File(argv[1],argv[2])
    
    if(bRet==True):
        print("file are same")
    else:
        print("file are not same")

if __name__=="__main__":
    main()
