'''
@Author:Naveen Madev Naik
@Date: 2024-07-22 13:21:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2021-02-11 18:00:30
@Title : Harmonic Number
'''
def harmonicNumber(number):
    """
    Description:
        this will return the Nth harmonic number
    Parameter:
        number:function will use this arguement to return harmonic number of this arguement
    Return:
        float

    """ 
    sum=0
    for num in range(1,number+1):
        sum+=1/num

    return sum    




try:
    number = int(input("Enter a number to calculate harmonic number: "))
    if number<1:
        print(f"Number {number} is out of bound")
    else:
        print(f"{number}th harmonic value is {harmonicNumber(number)}")
        
except ValueError:
    print("Please enter a valid integer number.")