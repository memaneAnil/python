def minimum(Input_Data):
    min=0
    for no in Input_Data:
        if(min>no):
            min=no

    return min

def main():
    Input_Data=[]

    iSize=0
    print("Enter how many elements you want")

    iSize=int(input())

    print("Enter the elements")

    for no in range(0,iSize,1):
        Input_Data.append(int(input()))
    
    Result=minimum(Input_Data)

    print("Minimum no is",Result)

if(__name__=="__main__"):
    main()