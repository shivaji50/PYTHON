# A Program to aceept a integer number list from a user and search the element in that list

list=eval(input("Enter the integer list: "))

print("The entered list is:",list)

search=input("Enter the element to check :")

for i in list:
	if i == int(search):
		print("Element is there in the list")
		break
else:
    print("Element is not there in the list")		
