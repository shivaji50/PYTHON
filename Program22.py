# A Python program to take maximum and minimum number and display even number in that range (Using while loop)

m=int(input("Enter the Minimum number :"))
n=int(input("Enter the Maximum number :"))

if m % 2 != 0:
	m=m+1

while m <= n:
	print(m)
	m=m+2
