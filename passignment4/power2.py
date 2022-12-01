def Double(no):
    return no*no

power=lambda iNo: iNo*iNo

def main():
    print("Enter the number")
    iNo=int(input())
    Result=0

    Result=Double(iNo)
    print("numbers power of 2 is:",Result)

    Ans=power(iNo)

    print("power of 2 using lambda",Ans)


if(__name__=="__main__"):
    main()
