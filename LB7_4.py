# a program which accept number from user and return multiplication of all 
# digits.   
# Input  : 2395
# Output : 270
# Function name : Dig()
# Author : Shivaji Das
# Date :  31 august 2021


def Dig(no):
    Mult=1
    if no < 0:
        no=-(no)

    while no > 0:
        idigit=int(no%10)
        if idigit==0:
            pass
        else:    
            Mult=Mult*idigit
        no=int(no/10)

    return Mult

def main():
    num=int(input("Enter the number :"))
    ret=Dig(num)
    print("The Multiplication of digit is :",ret)


if __name__=="__main__":
    main()     
             