'''

@Author:Naveen Madev Naik
@Date: 2024-07-23 11:41:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-23 11:41:00
@Title :program to check Perfect Number 

'''

   
def is_perfect_number(number):
    """
    Description:
        this function will return true if its perfect number and false if its not
    Parameter:
        number:use this parameter to check whether it is a perfect number
    Return:
       boolean

    """ 
    perfect_sum=0
    for divisor in range(1,(number//2)+1):
        if number%divisor==0:
         perfect_sum+=divisor
        else:
            pass
    if perfect_sum==number:
        return True
    else:
        return False
    




# Input from user
try:
    number = int(input("Enter a Number to check perfect number: "))
    if number==0:
        print(f"The number {number} is not Perfect Number ")
    elif is_perfect_number(number):
        print(f"The Number {number} is Perfect Number")
    else:
        print(f"The Number {number} is not Perfect Number")    
        
        
except ValueError:
    print("Please enter a valid integer year.")

