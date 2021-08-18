# a program which accept one number from user and print that number of 
# even numbers on screen.

# Input  : 7
# Output : 2 4 6 8 10 12 14 
# Function name : Even()
# Author : Shivaji Das
# Date : 18 august 2021

def Even(no):

    sum=0
    for i in range(no):
        sum=sum+2
        print(sum,end=" ") 


def main():
    x=int(input("Enter the number :"))
    Even(x)        


if __name__=="__main__":
    main()

