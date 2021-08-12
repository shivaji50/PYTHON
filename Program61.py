# A program to compare two arrays and display the boolean result

from numpy import *
a=array([1,2,3,0])
b=array([0,2,3,1])

c=a==b
print("Result of a==b:",c)
c=a>b
print("Result of a>b:",c)
c=a<=b
print("Result of a<=b:",c)