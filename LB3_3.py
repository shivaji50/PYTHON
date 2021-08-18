# a program which accept number from user and print even factors of that 
# number.  

# Input  : 36
# Output : 2 4 6 12 18  
# Function name : Factors()
# Author : Shivaji Das
# Date : 18 august 2021

def Factors(no):

    if(no<=0):
        return

    for i in range(1,no):
        if no%i==0 and i%2==0:
            print(i,end=" ")


def main():
    x=int(input("Enter the number :"))
    Factors(x)

if __name__=="__main__":
    main()                 