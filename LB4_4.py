# a program which accept number from user and return summation of all its 
# non factors.  

# Input  : 12
# Output : 50
# Function name : Factor()
# Author : Shivaji Das
# Date :  21 august 2021

def Factor(no):
    sum=0
    if no <= 0:
        return

    for i in range(1,no):
        if no%i!=0:
           sum=sum+i

    return sum       
            


def main():
    x=int(input("Enter the number :"))
    ret=Factor(x)
    print("The Summation of non factor is :",ret)
            


if __name__=="__main__":
    main() 