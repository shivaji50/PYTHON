# A program to know the effect of any() and all() function

from numpy import *
a=array([1,2,3,0])
b=array([0,2,3,1])

c=a>b
print("Result of a>b:",c)

print('Check if any one element is true:',any(c))
print('Check if all elements are true:',all(c))