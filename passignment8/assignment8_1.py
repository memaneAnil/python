def DisplayPattern1(iNo):
    if(iNo>0):
        print(" * ",end="")
        iNo=iNo-1
        DisplayPattern1(iNo)

def main():
    print("Enter the number")
    iValue=int(input())
    DisplayPattern1(iValue)


if __name__=="__main__":
    main()