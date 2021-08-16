# A program to calculate the factorial of a given number
def fact(n):
    prod=1
    while n>=1:
        prod=prod*n
        n=n-1
    return prod    


num=int(input("Enter the number to Find its factoial"))
x=fact(num)  
print("The factorial of the given number is:",x)  