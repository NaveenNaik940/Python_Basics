'''

@Author:Naveen Madev Naik
@Date: 2024-07-23 11:41:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-23 11:41:00
@Title :program to reverse the given number

'''

   
def reverse_number(number):
    """
    Description:
        this function will return reversed number 
    Parameter:
        number: using this number will reverse it 
    Return:
       int

    """
    reverse_number=0 
    while number>0:
        reverse_number=reverse_number*10 + number%10
        number//=10
    return reverse_number    


# Input from the user
try:
    number = int(input("Enter a number to reverse: "))
    print(f"Reversed number is: {reverse_number(number)}")

except ValueError:
    print("Invalid input. Please enter an integer.")


 







