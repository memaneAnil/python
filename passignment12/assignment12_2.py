import psutil
import os
from sys import *

def checkProcessRunning(processname):
    
    for proc in psutil.process_iter():
        try:
            if(processname.lower() in proc.name().lower()):
                pinfo=proc.as_dict(attrs=['pid','name','username'])
                break
            else:
                continue
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    if(len(pinfo)>0):
        return True,pinfo
    
def main():
    print("Marvellous Infosystem: Python automation and machine learning")

    print("process Monitor to check particular process")

    
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
        bret1,bret2=checkProcessRunning(argv[1])
        if(bret1==True): 
            print(bret2)
    except ValueError:
        print("Error : Invalid datatype of input")    
    except Exception:
        print("Error:process is not running")    

if __name__=="__main__":
    main()