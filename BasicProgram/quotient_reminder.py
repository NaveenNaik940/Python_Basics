'''
@Author:Naveen Madev Naik
@Date: 2024-07-22 13:21:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2021-02-11 18:00:30
@Title : compute quotient and reminder
'''

def compute_quotient_and_remainder(dividend, divisor):
    """
    Description:
         this function will return quotient and remainder
    Parameter:
         dividend,divisor: using this parameter we will find quotuent and remainder
    return:
       string          
    """
    if divisor == 0:
        return "Error: Division by zero is not allowed."
    
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    return quotient, remainder


try:
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
        
    result = compute_quotient_and_remainder(dividend, divisor)
        
    if isinstance(result, str):
        print(result)  # Error message
    else:
        quotient, remainder = result
        print(f"Quotient: {quotient}")
        print(f"Remainder: {remainder}")
            
except ValueError:
    print("Please enter valid integers.")


