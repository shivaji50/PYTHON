# a program which accept number from user and display its multiplication of 
# factors.   

# Input  : 12
# Output : 144 (1 * 2 * 3 * 4 * 6) 
# Function name : Factor()
# Author : Shivaji Das
# Date :  21 august 2021

def Factor(no):
    mult=1
    if no <= 0:
        return

    for i in range(1,no):
        if no%i==0:
            mult=mult*i   

    return mult

def main():
    x=int(input("Enter the number :"))
    ret=Factor(x)
    print("The output is :",ret)             


if __name__=="__main__":
    main() 