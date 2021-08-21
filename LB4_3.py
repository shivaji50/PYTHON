# a program which accept number from user and display all its non factors. 
    

# Input  : 12
# Output : 5 7 8 9 10 11
# Function name : Factor()
# Author : Shivaji Das
# Date :  21 august 2021

def Factor(no):
    mult=1
    if no <= 0:
        return

    for i in range(1,no):
        if no%i!=0:
            print(i,end=" ")
            


def main():
    x=int(input("Enter the number :"))
    Factor(x)
            


if __name__=="__main__":
    main() 