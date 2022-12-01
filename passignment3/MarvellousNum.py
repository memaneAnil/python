def ChkPrime(no):
    counter=0
    flag=False
    for iCnt in range(1,int(no/2+1),1):
        
        if(no%iCnt==0):
            counter=counter+1
              
    if(counter==1):
        flag=True
        return flag,no
    else:
        flag=False
        return flag,no