# A program to generate Fibonacci series

n = int(input('How many Fibonacci ?'))

f1=0
f2=1
c=2

if n == 1:
	print(f1)
elif n == 2:
    print(f1,'\n',f2,sep='')
else:
    print(f1,'\n',f2,sep='')
    while c < n:
        f = f1+f2
        print(f)
        f1=f2
        f2=f
        c=c+1    	