# A program to display and find the sum of a list of numbers using (Using while loop)

list=[10,20,30,40,50]
i=0
sum=0
while i < len(list):
	print(list[i])
	sum=sum+list[i]
	i=i+1

print("Sum =",sum)	