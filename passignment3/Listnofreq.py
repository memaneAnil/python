def numberfrequency(Input_Data,iSearchNo):
    
    iCnt=0
    for no in Input_Data:
        if(iSearchNo==no):
            iCnt=iCnt+1

    return iCnt

def main():
    Input_Data=[]

    iSize=0

    iSearchNo=0

    print("Enter how many elements you want")

    iSize=int(input())

    print("Enter the elements")

    for no in range(0,iSize,1):
        Input_Data.append(int(input()))

    
    print("Enter the no to search in List")

    iSearchNo=int(input())

    Result= numberfrequency(Input_Data,iSearchNo)

    print("Frequency of no in list is",Result)

if(__name__=="__main__"):
    main()