# A Python program to display command line arguments

import sys

n=len(sys.argv)   #display no of arguments

args=sys.argv

print('No of command line arguments are :',n)

print('The arguments are :',args)

print('The arguments one by one are')
for i in args:
	print(i) 
