# a program which accept number from user and count frequency of such a 
# digits which are less than 6. 
# Input  : 2395
# Output : 3
# Function name : Digit()
# Author : Shivaji Das
# Date :  24 august 2021

def Digit(no):
    cnt=0
    if no < 0:
        no=-(no)
    while no > 0:
        digit=int(no%10)
        if digit<6:
            cnt=cnt+1
        no=int(no/10)
    
    return cnt


def main():
    num=int(input("Enter the number :"))
    ret=Digit(num)
    print("The Frequency of less the 6 is :",ret)


if __name__=="__main__":
    main()     
