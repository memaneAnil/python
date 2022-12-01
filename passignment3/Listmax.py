def maximum(Input_Data):
    max=0
    for no in Input_Data:
        if(max<no):
            max=no

    return max

def main():
    Input_Data=[]

    iSize=0
    print("Enter how many elements you want")

    iSize=int(input())

    print("Enter the elements")

    for no in range(0,iSize,1):
        Input_Data.append(int(input()))
    
    Result=maximum(Input_Data)

    print("Maximum no is",Result)

if(__name__=="__main__"):
    main()