# A Program to display prime number series

max = int(input("Upto what number ?"))

for num in range(2, max+1):
	for i in range(2,num):
		if(num % i) == 0:
			break
		else:
			print(num)
			break
	        	