# A python program thats help to know the effects of slicing operations in array

from array import *

a = array('i',[10,20,30,40,50,60,70])

b=a[1:4]
print(b)

b=a[0:]
print(b)

b=a[:4]
print(b)

b=a[:-4]
print(b)

b=a[-4:-1]
print(b)

b=a[0:7:2]
print(b)
