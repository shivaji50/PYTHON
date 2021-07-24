# A program to short array elements using bubble short

from array import *

x =  array('i',[])

print("How many elements? ")
n = int(input())

for i in range(n):
	print('Enter elements',end='')
	x.append(int(input()))

print('Original array: ', x)

flag = False

for i in range(n-1):
	for j in range(n-1-i):
		if x[j] > x[j+1]:
			t = x[j]
			x[j] = x[j+1]
			x[j+1] =t
			flag = True
	if flag == False:
		break
	else:
	    flag = False

print('Sorted array= ',x)

			