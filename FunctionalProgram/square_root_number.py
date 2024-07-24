'''

@Author: Naveen Madev Naik
@Date: 2024-07-23 15:40:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-24 11:08:00
@Title :Program to compute the square root of a nonnegative number using Newton's method

'''


def newton_sqrt(c, tolerance=1e-10):
    """
    Description:
          Function to compute the square root of a nonnegative number using Newton's method.
    Parameters:
        c: float, the number to find the square root of
        tolerance: float, the tolerance for the convergence of the method
    Returns:
       float: approximate square root of c
    """
    if c < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    if c == 0:
        return 0
    
    # Initial guess
    x = c
    
    while True:
        # Compute the next approximation
        next_x = 0.5 * (x + c / x)
        
        # Check for convergence
        if abs(next_x - x) < tolerance:
            break
        
        # Updating the current approximation
        x = next_x
    
    return x

def main():
    
    try:
        c = float(input("Enter a nonnegative number to find the square root of: "))
        if c < 0:
            raise ValueError("Input must be a nonnegative number.")
        
        sqrt_c = newton_sqrt(c)
        print(f"The square root of {c} is approximately {sqrt_c:.10f}")
        
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
