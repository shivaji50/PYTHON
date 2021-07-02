# Program to create bytearray type array and display,Modify all its elements

elements=[10,20,30,40,50]

#converting the list into bytearray type array
x=bytearray(elements)

print('Before Modification')
for i in x:print(i)

x[0]=100
x[2]=250

print('After Modification')
for i in x:print(i)

