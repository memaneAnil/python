def Display(iNo):
    if(iNo>0):
        print(" * ",end="")
        iNo=iNo-1
        Display(iNo)

def main():
    print("Enter the number")
    iValue=int(input())
    Display(iValue)


if __name__=="__main__":
    main()