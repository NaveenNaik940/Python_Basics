'''

@Author:Naveen Madev Naik
@Date: 2024-07-23 11:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-23 11:00:00
@Title : program to find Fibonacci Series

'''

   
def fibonacci_number(limit):
    """
    Description:
        this function will return fibonacci numbers till given number
    Parameter:
        limit:this parameter used to set the limit
    Return:
        list

    """ 
    a,b=0,1
    fibonacci_series=[]
    while a<=number:
        fibonacci_series.append(a)
        a,b=b,a+b
    return fibonacci_series

# Input from user
try:
    number = int(input("Enter a Number to print Fibonacci Numbers: "))
    if number==0:
        print(f"Fibonacci Numbers are: {0} ")
    else:
        print(f"Fibonacci numbers are:{ fibonacci_number(number)}")
        
except ValueError:
    print("Please enter a valid integer year.")

