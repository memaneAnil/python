import os.path
def Display(filename):
    if(os.path.exists(filename)):
        f=open(filename,'r')
        print(f.read())

def main():
    print("Enter the file name")
    fname=input()
    Display(fname)   

if __name__=="__main__":
    main()