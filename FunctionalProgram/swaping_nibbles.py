'''

@Author: Naveen Madev Naik
@Date: 2024-07-23 16:57:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-24 11:08:00
@Title :Program to convert a decimal number and swaping nibbles and checking decimal of swapped nibbles is power of 2

'''


import math 

def to_binary(number):
    """
    Description:
        Function to convert a decimal number to its binary representation.
    Parameters:
        number: int, the decimal number to convert
    Returns:
        list of length 8
    """
    if number < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    
    binary_digits = []
    
    # Handeling the special case where the number is zero
    if number == 0:
        binary_digits.append(0)
    
    
    while number > 0:
        binary_digits.append(number % 2)
        number //= 2
    if len(binary_digits)==8:
        pass
    else: 
        while len(binary_digits)!=8:
            binary_digits.append(0)    
    
    binary_digits.reverse()
    

    
    return binary_digits

def swap_nibbles_check_power_of_two(binary_digits):
    """
    Description:
         This function will swap the nibbles and check the decimal of swapped nibble is power of two

    Parameter:
         binary_digits: binary converted decimal used for swaping

    return:
         int: resultant number
         boolean:is_power_of_two()               
    """
    binary_digits[0:4],binary_digits[4:8]=binary_digits[4:8],binary_digits[0:4]
    resultant_number=0

    for binary in range(len(binary_digits)):
        resultant_number+=binary_digits[binary]*2**binary

    return resultant_number,is_power_of_two(resultant_number)    

    

def is_power_of_two(number):
    """
    Description:
          this function will check whether givennumber is power of two
    Parameter:
          number:will check this number is power of two or not
    return:
          boolean            
    """
    if number <= 0:
        return False
    
    log_value = math.log2(number)
    
    return log_value.is_integer()

def main():
    try:
        decimal_number = int(input("Enter a non-negative integer: "))
        if decimal_number < 0:
            raise ValueError("Input must be a non-negative integer.")
        
        binary_representation = to_binary(decimal_number)
        
        binary_str = ''
        for digit in binary_representation:
            binary_str += str(digit)
    
   
        padded_binary_str = binary_str.zfill(32)
        print(f"binary converted format of decimal {decimal_number} is {padded_binary_str}")
        swaped_decimal,powerOfTwo=swap_nibbles_check_power_of_two(binary_representation)
        print(f"decimal after swaping nibles of {decimal_number} is {swaped_decimal}")
        if powerOfTwo:
            print(f"{swaped_decimal} is power of 2")
        else:
            print(f"{swaped_decimal} is not power of 2")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
