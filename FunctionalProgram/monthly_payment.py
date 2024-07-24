'''

@Author: Naveen Madev Naik
@Date: 2024-07-23 16:00:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-24 11:09:00
@Title :Program to calculate the monthly payments for a loan

'''


def calculate_monthly_payment(principal, years, annual_rate):
    """
    Description:
          Function to calculate monthly payment for a loan.
    Parameters:
        principal: float, the principal loan amount
        years: int, the number of years to pay off the loan
        annual_rate: float, the annual interest rate
    Returns:
       float: monthly payment
    """
    # Convert annual rate to a monthly rate
    monthly_rate = annual_rate / 100 / 12
    # Total number of monthly payments
    num_payments = years * 12
    
    # Calculating the monthly payment using the formula
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
    
    return monthly_payment

def main():
    
    try:
        
        principal = float(input("Enter the principal loan amount: "))
        years = int(input("enter the year: "))
        annual_rate = float(input("Enter the loan intrest rate: "))
        
        if principal <= 0 or years <= 0 or annual_rate <= 0:
            raise ValueError("All inputs must be positive numbers.")
        
        monthly_payment = calculate_monthly_payment(principal, years, annual_rate)
        print(f"The monthly payment is: {monthly_payment:.2f}")
        
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
