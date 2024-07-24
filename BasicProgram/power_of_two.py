'''
@Author:Naveen Madev Naik
@Date: 2024-07-22 13:21:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2021-02-11 18:00:30
@Title : Power of 2
'''
def power_of_two(number):
    """
    Description:
        this function will print the power of two till specified number
    Parameter:
        number:  used to get the power of 2 till that arguement
    Return:
        none

    """    
    for num in range(number+1):
        print(f"{2**num}")

try:
    number = int(input("Enter a Number: "))
    if number>31:
        print(f"Number {number} is out of bound")
    else:
        power_of_two(number)
except ValueError:
    print("Please enter a valid integer number.")