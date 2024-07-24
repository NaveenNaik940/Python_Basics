'''
@Author:Naveen Madev Naik
@Date: 2024-07-22 13:21:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2021-02-11 18:00:30
@Title :check odd or even
'''
def check_even_odd(number):
    """
    Description:
         this function will return whether number is odd or even
    Parameter:
         number: it is used to check , whether it is odd or even
    return:
       string          
    """    
    if number % 2 == 0:
        return f"{number} is Even."
    else:
        return f"{number} is Odd."

try:
   number=int(input("Enter the nunber to check Odd or Even: "))
   result = check_even_odd(number)  
   print(result)  
except ValueError:
    print("Enter the possitive Integer value")   