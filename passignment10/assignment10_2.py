import os
from sys import *
import pathlib

def DirectoryWatcher(path,ext1,ext2):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists:
               
        for foldername,subfolder,FileNames in os.walk(path):
            
            for fname in FileNames:
                if(fname.endswith(ext1)):
                   
                    path=os.path.join(foldername,fname)
                    print(path)
                    tname,ext=os.path.splitext(fname)
                    
                    path2=os.path.join(foldername,tname+ext2)
                    os.rename(path,path2)             
                    
            print("")

    else:
        print("Invalid Path")

def main():
    print("Directory watcher application")
    if(len(argv)!=4):
        print("Insufficient arguments")
        exit()
    if(argv[1]=='-h'):
        print("this script will travel the directory and display the names of all entries")
        exit()
    if (argv[1]=='-u'):
        print("usage : Application_name Directory_name")
        exit()

    try:
        DirectoryWatcher(argv[1],argv[2],argv[3])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")



if __name__=="__main__":
    main()