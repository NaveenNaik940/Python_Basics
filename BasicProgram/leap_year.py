 
'''
@Author:Naveen Madev Naik
@Date: 2024-07-22 13:21:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2021-02-11 18:00:30
@Title : Leap Year
'''
   




def is_leap_year(year):
    """
    Description:
        this function will return whether entered year is leaf year of not
    Parameter:
        year:it is used to check leaf year
    Return:
        Boolean: True or False

    """     
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Input from user
try:
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Please enter a valid integer year.")

