# A program to position of an elements in an array using sequential search

from array import *

x = array('i',[])

print('How Many elements?')
n = int(input())

for i in range(n):
	print('Enter elements ',end='')
	x.append(int(input()))

print('Original array: ',x)

print("Enter element to bi searched: ",end='')
search = int(input())

flag = False

for i in range(n):
    if search == x[i]:
        print("Found at Position= ",i+1)
        flag = True	

if flag == False:
    print('Not Found in the array')        