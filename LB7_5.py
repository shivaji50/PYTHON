# a program which accept number from user and return difference between 
# summation of even digits and summation of odd digits.   
# Input  : 2395
# Output : -15 (2 - 17) 
# Function name : Dig()
# Author : Shivaji Das
# Date :  31 august 2021


def Dig(no):
    sum1=0
    sum2=0
    if no < 0:
        no=-(no)

    while no > 0:
        idigit=int(no%10)
        if idigit%2==0:
            sum1=sum1+idigit
        else:
            sum2=sum2+idigit
        no=int(no/10)

    return sum1-sum2

def main():
    num=int(input("Enter the number :"))
    ret=Dig(num)
    print("The Difference is :",ret)


if __name__=="__main__":
    main()     
             