import os
from sys import *
import hashlib

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf= afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayChecksum(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists:
               
        for foldername,subfolder,FileNames in os.walk(path):
            print("Current folder is :",foldername)
            for fname in FileNames:
                path=os.path.join(foldername+"/"+fname)
                filehash=hashfile(path)
                print(path)
                print(filehash)
                print('')
        print("Error : Invalid number of arguments")
        exit()
        
    else:
        print("Invalid Path")
    
        
def main():

    print("Directory watcher application")
    if(len(argv)!=2):
        print("Insufficient arguments")
        exit()
    if(argv[1]=='-h'):
        print("this script will travel the directory and display the names of all entries")
        exit()
    if (argv[1]=='-u'):
        print("usage : Application_name Directory_name")
        exit()

    try:
        DisplayChecksum(argv[1])
    

if __name__=="__main__":
    main()