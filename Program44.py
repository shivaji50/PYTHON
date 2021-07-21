# A program to retrive elements of an array using array indexing---V2--using while loop

from array import *

a = array('i',[10,20,30,40])

n =len(a)

i = 0

while i < n:
	print(a[i],end=' ')
	i=i+1

