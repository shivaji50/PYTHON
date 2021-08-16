# A program to check a given number is prime or not
def prime(n):

    for i in range(2,n):
        if(n%i==0):
            x=0
            break
        else:
            x=1
    return x        




num=int(input("Enter the number to check its prime or not:"))
x=prime(num)
if(x==1):
    print("its a prime number")
else:
    print("its is not a prime number")    
