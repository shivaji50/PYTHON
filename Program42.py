# A program to create one array from another array and multiplying the elements 
# of first array by 3 before storing it into the second array

from array import *

arr1 = array('i',[100,200,300,400])
print('The first array ',arr1)

arr2 = array(arr1.typecode,(a * 3 for a in arr1))
print('The second array',arr2)
 