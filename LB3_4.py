# Accept one character from user and convert case of that character.  

# Input  : a , B
# Output : A , b  
# Function name : convert()
# Author : Shivaji Das
# Date : 18 august 2021

def convert(char):

    if char.isalpha()==False:
        print("wrong input")
        return

    if char.isupper()==True:
        x=char.lower()
        print("After converting",x)
    elif char.islower()==True:
        x=char.upper()
        print("After converting",x)


def main():
    x=input("Enter the character:")
    convert(x)

if __name__=="__main__":
    main()                 
