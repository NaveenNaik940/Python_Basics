'''
@Author:Naveen Madev Naik
@Date: 2024-07-22 13:21:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2021-02-11 18:00:30
@Title : prime factor
'''

def prime_factors(num):
    factors = []
    
    # Check for number of 2s that divide num
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    
    # Check for odd factors from 3 onwards
    factor= 3
    while factor * factor <= num:
        while num % factor == 0:
            factors.append(factor)
            num //= factor
        factor += 2  # Move to the next odd number
    
    # If num is a prime number greater than 2
    if num > 2:
        factors.append(num)
    
    return factors


try:
    number = int(input("Enter a number to find its prime factors: "))
    if number <= 0:
        print("Please enter a positive integer.")
    
        
    factors = prime_factors(number)
    print("Prime factors of", number, "are:", factors)
        
except ValueError:
    print("Please enter a valid integer.")


