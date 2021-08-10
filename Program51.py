# A program to position of an elements in an array using sequential search using index method--v2

from array import *
from typing import Any

x = array('i',[])

print('How Many elements?')
n = int(input())

for i in range(n):
	print('Enter elements ',end='')
	x.append(int(input()))

print('Original array: ',x)

print("Enter element to bi searched: ",end='')
search = int(input())

try:
    pos = x.index(search)
    print('Found at position=',pos)

except valueError:
    print('Not found in the array')          