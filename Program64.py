# A program to retrive non-zero elements from an array

from numpy import *
a=array([1,2,0,-1,0,6])
c=nonzero(a)

for i in c:
    print(i)  # displays indexes

print(a[c]) # display the non-zero elements     