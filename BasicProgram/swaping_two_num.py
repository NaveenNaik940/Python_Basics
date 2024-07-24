'''
@Author:Naveen Madev Naik
@Date: 2024-07-22 13:21:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2021-02-11 18:00:30
@Title : Swaping two number
'''

def swap_two_number(num1,num2):
    """
    Description:
          this function only swap two number
    parameter:
        num1,num2: this are the arguements that will eventualy get swapped
    return:
        tuple          
    """
    num1=num2+num1

    num2=num1-num2

    num1=num1-num2
    return num1,num2

try:
    number1=int(input("Enter the first number"))
    number2=int(input("Enter the second number"))
    number1,number2=swap_two_number(number1,number2)
    print(f"After Swaping Number1:{number1} and Number2:{number2}")

except ValueError:
    print("Enter the integer value:")    