# Accept different number system from user and convert
# it into decimal number and display

# This is option 1
str=input('Enter the Hexadecimal number:')
print('After converting',int(str,16))

# This can be option 2
str=input('\nEnter the Octal number:')
x=int(str,8)
print('After converting',x)

str=input('\nEnter the Binary number:')
print('After converting',int(str,2))