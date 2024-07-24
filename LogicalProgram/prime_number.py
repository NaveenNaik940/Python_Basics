'''

@Author:Naveen Madev Naik
@Date: 2024-07-23 11:41:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-23 11:41:00
@Title :program to find Prime Number 

'''

   
def is_prime(num):
    """
    Description:
        this function will return true if its prime number and false if its not
    Parameter:
        num: parameter to check whether it is a prime number
    Return:
       boolean

    """     
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    factor = 5
    while factor * factor <= num:
        if num % factor == 0 or num % (factor + 2) == 0:
            return False
        factor += 6
    return True

# Input from the user
try:
    number = int(input("Enter a number to check if it is prime: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter an integer.")


 







