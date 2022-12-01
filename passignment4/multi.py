def Multi(no1,no2):
    return no1*no2

MultiFunction=lambda iNo1,iNo2: iNo1*iNo2

def main():
    print("Enter the first number")
    iNo1=int(input())
    Result=0

    print("Enter the second number")
    iNo2=int(input())

    Result=Multi(iNo1,iNo2)
    print("Multification of number is:",Result)

    Ans=MultiFunction(iNo1,iNo2)

    print("Multification of number using lambda",Ans)


if(__name__=="__main__"):
    main()
