# A Program to know the effect of view() method

from numpy import *
a=arange(1,6)
b=a.view()
print("Original array:",a)
print("New array:",b)

b[0]=99

print("After modification")
print("Original array:",a)
print("New array:",b)