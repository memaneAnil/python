
def SumOfDigit(iNo,iSum):
    digit=0
    
    if(iNo>0):
        digit=iNo%10
        iSum=iSum+digit
        
        iNo=int(iNo/10)
        return SumOfDigit(iNo,iSum)
    
        
        
def main():
    iSum=0
    
    print("Enter the number")
    iValue=int(input())
    add=SumOfDigit(iValue,iSum)
    print(add)

if __name__=="__main__":
    main()