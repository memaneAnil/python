import os
from sys import *
import pathlib

def DirectoryWatcher(path,ext):

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists:
               
        for foldername,subfolder,FileNames in os.walk(path):
            
            for fname in FileNames:
                if(fname.endswith(ext)):
                    print("File inside folder"+foldername+" is "+fname)
    
            print("")

    else:
        print("Invalid Path")

def main():
    print("Directory watcher application")
    if(len(argv)!=3):
        print("Insufficient arguments")
        exit()
    if(argv[1]=='-h'):
        print("this script will travel the directory and display the names of all entries")
        exit()
    if (argv[1]=='-u'):
        print("usage : Application_name Directory_name")
        exit()

    try:
        DirectoryWatcher(argv[1],argv[2])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")



if __name__=="__main__":
    main()