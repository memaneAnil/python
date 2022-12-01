
import os
from sys import *
import hashlib
import time
import os.path

def DeleteFiles(dict1):
    results=list(filter(lambda x: len(x)>1,dict1.values())) 

    if len(results)>0:
        print("Duplicates Found :")

        print("The following files are identical.")

        if not os.path.exists("Log.txt"):
            try:
                fd=open("Log.txt",'w')
                print("file created in write mode")
            except:
                pass
        else:
            fd=open("Log.txt",'a')
            print("file created in append mode")
            print(fd)
            icnt=0

        print("_______")
        icnt=0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    print(subresult+"\n")
                    fd.write("%s\n" % subresult)
                    #fd.write(subresult)
                    os.remove(subresult)
        icnt=0

    else:
        print("No duplicate files found")
    
def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf= afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def FindDuplicate(path):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups={}
    
    if exists:
               
        for dirName,subdirs,FileList in os.walk(path):
            print("Current folder is :",dirName)
            for fname in FileList:
                path=os.path.join(dirName+"/"+fname)
                filehash=hashfile(path)

                if filehash in dups:
                    dups[filehash].append(path)
                else:
                    dups[filehash]=[path]
        return dups
        print("Error : Invalid number of arguments")
        exit()
        
    else:
        print("Invalid Path")

def printDuplicate(dict1):
    results=list(filter(lambda x: len(x)>1,dict1.values())) 

    if len(results)>0:
        print("Duplicates Found :")

        print("The following files are identical.")

        icnt=0
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    print("\t\t%s"% subresult)

        
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
        arr={}
        startTime=time.time()
        arr=FindDuplicate(argv[1])
        printDuplicate(arr)
        DeleteFiles(arr)
        endTime=time.time()

        print("Took %s second to evaluate"%(endTime-startTime))

    except ValueError:
        print("Error: Invalid datatype of input")

if __name__=="__main__":
    main()