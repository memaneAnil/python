import MarvellousNum

def ListPrime(Input_Data):
    add=0
    flag=False
    rno=0
    for no in Input_Data:
        flag,rno=MarvellousNum.ChkPrime(no)
        if(flag==True):
            add=add+rno
            
    return add

def main():
    Input_Data=[]

    iSize=0
    print("Enter how many elements you want")

    iSize=int(input())

    print("Enter the elements")

    for no in range(0,iSize,1):
        Input_Data.append(int(input()))
    
    
    Result=ListPrime(Input_Data)

    if(Result!=0):
        print("addition of prime no form list is ",Result)
    else:
        print("list does not contain any prime no")
if(__name__=="__main__"):
    main()