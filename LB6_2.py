# e a program which accept number from user and check whether it contains 0 
# in it or not.   

# Input  : 2395
# Output : There is no Zero
# Function name : Digit()
# Author : Shivaji Das
# Date :  24 august 2021

def Digit(no):

    if no < 0:
        no=-(no)
    while no > 0:
        digit=int(no%10)
        if digit==0:
            no=1
            break
        no=int(no/10)
    
    if no==1:
        return True
    else: 
        return False 


def main():
    num=int(input("Enter the number :"))
    ret=Digit(num)
    if ret==True:
        print("The Digit contains Zero")
    else:
        print("Thw Digit does not contain Zero")    


if __name__=="__main__":
    main()     
