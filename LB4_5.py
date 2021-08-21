# a program which accept number from user and return difference between 
# summation of all its factors and non factors. 

# Input  : 12
# Output : -34 (16 - 50) 
# Function name : Factor()
# Author : Shivaji Das
# Date :  21 august 2021

def Factor(no):
    sum1,sum2=0,0
    if no <= 0:
        return

    for i in range(1,no):
        if no%i!=0:
           sum2=sum2+i
        else:
            sum1=sum1+i   

    return sum1-sum2      
            


def main():
    x=int(input("Enter the number :"))
    ret=Factor(x)
    print("The Difference is :",ret)
            


if __name__=="__main__":
    main() 