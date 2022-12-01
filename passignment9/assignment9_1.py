import os.path
def Check(filename):
    if(os.path.exists(filename)):
        return True

def main():
    print("Enter the file name")
    fname=input()
    bRet=Check(fname)

    if(bRet==True):
        print("file exists in current directory")
    else:
        print("file not exists in current directory")

if __name__=="__main__":
    main()
