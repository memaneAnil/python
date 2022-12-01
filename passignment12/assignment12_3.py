import os
import psutil
import time
from sys import *
import os

def ProcessDisplay(log_dir="Marvellous"):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator="_"*80
    log_path=os.path.join(log_dir,"Marvellous%s.log"%(time.ctime()))
    f=open(log_path,'w')
    f.write(separator+ "\n")
    f.write("Marvellous Infosystem process Logger : "+time.ctime()+ "\n")
    f.write(separator+ "\n")

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass


        for element in listprocess:
            f.write("%s\n" % element)

def main():
    print("___________Marvellous Infosytem by Piyush Khairnar__________")

    print("Application name :"+argv[0])

    if(len(argv)!=2):
        print("Error: Invalid number of arguments")
        exit()

    if((argv[1]=='-h') or (argv[1]=='-H')):
        print("Help : This script is used log record of running processes")
        exit()

    if((argv[1]=='-u') or (argv[1]=='-U')):
        print("usage: Application name Absoulute path of directory")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")


if __name__=="__main__":
    main()