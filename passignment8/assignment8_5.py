def fact(iNo):
    if(iNo==1):
        return 1
    return iNo*fact(iNo-1)  
        
def main():
    
    print("Enter the number")
    iValue=int(input())
    iRet=fact(iValue)
    print(iRet)


if __name__=="__main__":
    main()











#def Factorial(iNo,fact):
       
#    if(iNo>0):
#        fact=fact*iNo
#        iNo=iNo-1
#       Factorial(iNo,fact)
#    else:
#        print(fact)       