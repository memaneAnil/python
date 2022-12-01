def DisplayPattern(iNo):
    
    if(iNo>0):
        print(iNo,end="   ")
        DisplayPattern(iNo-1)
        
def main():
    print("Enter the number")
    iValue=int(input())
    DisplayPattern(iValue)


if __name__=="__main__":
    main()