'''

@Author:Naveen Madev Naik
@Date: 2024-07-23 11:41:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-23 11:41:00
@Title :program to generate a coupon number

'''


import random

class CouponSimulator:
    
    @staticmethod
    def generate_random_coupon(max_coupon):
        """
    Description:
        this function will Generate a random coupon number between 0 and max_coupon - 1. 
    Parameter:
        max_coupon: max_coupon represents the total number of distinct coupon types available
    Return:
       int

    """        
        """Generate a random coupon number between 0 and max_coupon - 1."""
        return random.randint(0, max_coupon - 1)
    
    @staticmethod
    def count_random_numbers_for_distinct_coupons(n):
        """
    Description:
        this function will return process to determine how many random numbers are needed to get all distinct coupons 
    Parameter:
        n: n distinct coupons 
    Return:
       int

    """    

        collected_coupons = set()
        total_draws = 0
        
        while len(collected_coupons) < n:
            coupon = CouponSimulator.generate_random_coupon(n)
            collected_coupons.add(coupon)
            total_draws += 1
        
        return total_draws

# Input from the user
try:
    num_coupons = int(input("Enter the number of distinct coupon numbers (N): "))
    if num_coupons <= 0:
        print("The number of coupons should be a positive integer.")
    else:
        total_draws = CouponSimulator.count_random_numbers_for_distinct_coupons(num_coupons)
        print(f"Total random numbers needed to get all {num_coupons} distinct coupons: {total_draws}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
