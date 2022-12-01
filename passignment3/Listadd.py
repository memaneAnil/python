def addition(Input_Data):
    add=0
    for no in Input_Data:
        add=add+no

    return add

def main():
    Input_Data=[]

    iSize=0
    print("Enter how many elements you want")

    iSize=int(input())

    print("Enter the elements")

    for no in range(0,iSize,1):
        Input_Data.append(int(input()))
    
    Result=addition(Input_Data)

    print("addition is",Result)

if(__name__=="__main__"):
    main()