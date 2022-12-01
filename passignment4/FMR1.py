def FilterNo(no):
    if((no>=70) and (no<=90)):
        return no
    
def AddNo(no):
    return no+10

def Product(Data):
    ans=1
    for no in Data:
        ans=ans*no

    return ans
    
def FilterListNo(Helper_Function,Data):
    
    filterlist=[]
    for no in Data:
        value=FilterNo(no)
        if(value!=None):
            filterlist.append(value)
    
    return filterlist


def MapListNo(Helper_Function,Data):
    Maplist=[]
    for no in Data:
        value=AddNo(no)
        Maplist.append(value)

    return Maplist


def ReduceListNo(Helper_Function,Data):
    ans=0
    ans=Product(Data)

    return ans


def main():
    Data_Input=[]

    print("Enter the number of element store in List")
    iSize=int(input())



    print("Enter the number")

    for no in range(0,iSize,1):
        No=int(input())
        Data_Input.append(No)

    Filtered_List=FilterListNo(FilterNo,Data_Input)

    print("filtered list is :",Filtered_List)

    Maplist=MapListNo(AddNo,Filtered_List)

    print("map list is :",Maplist)

    product=ReduceListNo(Product,Maplist)

    print("product is :",product)



if(__name__=="__main__"):
    main()
