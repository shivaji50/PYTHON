# a program which accept number from user and display its factors in 
# decreasing order.    

# Input  : 12
# Output : 6 4 3 2 1 
# Function name : Factor()
# Author : Shivaji Das
# Date :  21 august 2021

def Factor(no):
    mult=1
    if no <= 0:
        return

    for i in reversed(range(1,no)):
        if no%i==0:
            print(i,end=" ")
            


def main():
    x=int(input("Enter the number :"))
    Factor(x)
            


if __name__=="__main__":
    main() 