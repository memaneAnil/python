import os.path
from sys import *

def file_copy(filename):
    f=open(filename,'r')
    fd=open("Demo.txt",'a')
    
    fd.write(f.read())
    
def main():
    
    fname=argv[1]
    file_copy(fname)   

if __name__=="__main__":
    main()