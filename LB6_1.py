# a program which accept number from user and display its digits in reverse 
# order.  

# Input  : 2395
# Output :  5 
#           9 
#           3 
#           2
# Function name : Digit()
# Author : Shivaji Das
# Date :  24 august 2021

def Digit(no):

    if no < 0:
        no=-(no)
    while no > 0:
        digit=int(no%10)
        print(digit)
        no=int(no/10)



def main():
    num=int(input("Enter the number :"))
    Digit(num)


if __name__=="__main__":
    main()     
