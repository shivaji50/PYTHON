# A program to perfrom some mathametical operation on numpy array

from numpy import *
arr=array([10,20,30.5,-40])
print("Original array=",arr)

print("After Adding=",arr+5)
print("After Substracting=",arr-5)
print("After Multiplying=",arr*5)
print("After dividing=",arr/5)
print("After moduls=",arr%5)

print("Biggest element: ",max(arr))
print("Smallest element: ",min(arr))
print("Sum of all elements: ",sum(arr))
print("Average of all elements ",mean(arr))