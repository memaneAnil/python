import MarvellousNum

def ChkPrimeNo(Input_Data):
    Filterlist=[]
    flag=False
    rno=0
    for no in Input_Data:
        flag,rno=MarvellousNum.ChkPrime(no)
        if(flag==True):
            Filterlist.append(rno)
            
    return Filterlist

    
def MulNo(no):
    return no*2

def MaxNo(Data):
    max=0
    for no in Data:
        if(max<no):
            max=no

    return max
    
def FilterListNo(Helper_Function,Data):
    
    
    filterlist=ChkPrimeNo(Data)
       
    return filterlist


def MapListNo(Helper_Function,Data):
    Maplist=[]
    for no in Data:
        value=MulNo(no)
        Maplist.append(value)

    return Maplist


def ReduceListNo(Helper_Function,Data):
    
    ans=MaxNo(Data)

    return ans


def main():
    Data_Input=[]

    print("Enter the number of element store in List")
    iSize=int(input())



    print("Enter the number")

    for no in range(0,iSize,1):
        No=int(input())
        Data_Input.append(No)

    Filtered_List=FilterListNo(ChkPrimeNo,Data_Input)

    print("filtered list is :",Filtered_List)

    Maplist=MapListNo(MulNo,Filtered_List)

    print("map list is :",Maplist)

    iMax=ReduceListNo(MaxNo,Maplist)

    print("product is :",iMax)



if(__name__=="__main__"):
    main()
