'''
@Author:Naveen Madev Naik
@Date: 2024-07-22 13:21:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2021-02-11 18:00:30
@Title :finding the largest number in three number
'''
def find_largest_of_three(num1, num2, num3):
    """
    Description:
         this function will return the largest of three number
    Parameter:
         num1,num2,num3: which will be used to compare
    return:
       string          
    """
    if num1 >= num2 and num1 >= num3:
        return f"The largest number is {num1}."
    elif num2 >= num1 and num2 >= num3:
        return f"The largest number is {num2}."
    else:
        return f"The largest number is {num3}."

try:
    number1=int(input("Enter the First Number"))
    number2=int(input("Enter the Second Number"))
    number3=int(input("Enter the Third Number"))
    result = find_largest_of_three(number1, number2, number3) 
    print(result)  
except ValueError:
    print("Enter the valid integer number")