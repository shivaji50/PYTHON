#  a program which accept number from user and return the count of even 
# digits.  
# Input  : 2395
# Output : 1
# Function name : Dig()
# Author : Shivaji Das
# Date :  31 august 2021


def Dig(no):
    cnt=0
    if no < 0:
        no=-(no)

    while no > 0:
        idigit=int(no%10)
        if idigit%2==0:
            cnt=cnt+1
        no=int(no/10)

    return cnt

def main():
    num=int(input("Enter the number :"))
    ret=Dig(num)
    print("The count of the even digit is :",ret)


if __name__=="__main__":
    main()     
             