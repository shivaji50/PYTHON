# A Python program to understand various method of array class

from array import *

arr = array("i",[10,20,30,40,50])
print('Original array:',arr)

arr.append(30)
arr.append(60)
print('After appending 30 and 60:',arr)

arr.insert(1,99)
print('After inserting 99 in first position:',arr)

arr.remove(20)
print('After removing 20:',arr)

n = arr.pop()
print('Array after usin pop():',arr)
print('Popped element:',n)

n = arr.index(30)
print('First occurance of elements 30 is at:',n)

lst = arr.tolist()
print('List: ',lst)
print('Array: ',arr)