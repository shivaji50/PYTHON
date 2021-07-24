# A Program to store students marks and find its total marks and percentage

from array import *

str = input('Enter marks: ').split(' ')

marks = array('i',[int(num) for num in str])

sum = 0
for x in marks:
	print(x)
	sum+=x
print('Total marks: ',sum)

n = len(marks)
percentage = sum/n	
print('percentage: ',percentage)