#  Accept on character from user and check whether that character is vowel or not

# Input  : a 
# Output : It is vowel 
# Function name : convert()
# Author : Shivaji Das
# Date : 18 august 2021

def convert(ch):

    if ch.isalpha()==False:
        print("wrong input")
        return

    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
    or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        return True
    else:
        return False    



def main():
    x=input("Enter the character:")
    ret=convert(x)
    if(ret==True):
        print("It is vowel")
    else:
        print("It is not a vowel")    

if __name__=="__main__":
    main()                 
