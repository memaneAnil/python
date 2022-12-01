def DisplayPattern(iNo):
    
    if(iNo>0):
        DisplayPattern(iNo-1)
        print(iNo,end="   ")
                
def main():
    print("Enter the number")
    iValue=int(input())
    DisplayPattern(iValue)


if __name__=="__main__":
    main()