 
'''
@Author:Naveen Madev Naik
@Date: 2024-07-22 13:21:00
@Last Modified by: Author Name
@Last Modified time: 2021-02-11 18:00:30
@Title : Flip Coin and print percentage of Heads and Tails
'''


import random

def flip_coin(times):
    """
    Description:
        this function prints the percentage of head and tail count
    Parameter:
        times: this is arguement which specifies how many times we need flip coin
    Return:
        none

    """    
    # Ensure the input is a positive integer
    if times <= 0 or not isinstance(times, int):
        print("The number of times to flip the coin should be a positive integer.")
        return

    heads = 0
    tails = 0

    for _ in range(times):
        if random.random() < 0.5:
            tails += 1
        else:
            heads += 1

    heads_percentage = (heads / times) * 100
    tails_percentage = (tails / times) * 100

    print(f"Heads: {heads} times ({heads_percentage:.2f}%)")
    print(f"Tails: {tails} times ({tails_percentage:.2f}%)")

# Get the number of times to flip the coin from the user
try:
    times = int(input("Enter the number of times to flip the coin: "))
    flip_coin(times)
except ValueError:
    print("Please enter a valid positive integer.")
