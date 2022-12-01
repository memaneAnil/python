def FilterEvenNo(no):
    if(no%2==0):
        return no
    
def Nosquare(no):
    return no*no

def addition(Data):
    ans=0
    for no in Data:
        ans=ans+no

    return ans
    
def FilterListNo(Helper_Function,Data):
    
    filterlist=[]
    for no in Data:
        value=FilterEvenNo(no)
        print(value)
        if(value!=None):
            filterlist.append(value)
    
    return filterlist


def MapListNo(Helper_Function,Data):
    Maplist=[]
    for no in Data:
        value=Nosquare(no)
        Maplist.append(value)

    return Maplist


def ReduceListNo(Helper_Function,Data):
    ans=0
    ans=addition(Data)

    return ans


def main():
    Data_Input=[]

    print("Enter the number of element store in List")
    iSize=int(input())



    print("Enter the number")

    for no in range(0,iSize,1):
        No=int(input())
        Data_Input.append(No)

    Filtered_List=FilterListNo(FilterEvenNo,Data_Input)

    print("filtered list is :",Filtered_List)

    Maplist=MapListNo(Nosquare,Filtered_List)

    print("map list is :",Maplist)

    add=ReduceListNo(addition,Maplist)

    print("product is :",add)



if(__name__=="__main__"):
    main()
