'''

@Author:Naveen Madev Naik
@Date: 2024-07-23 11:41:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-23 11:41:00
@Title :program to generate stop watch 

'''


import time

def stopwatch():
    """
    Description:
            this function is to measuring the time that elapses between
            the start and end clicks
    Parameter:
       None
    return:
       None           
    """
    input("Press Enter to start the stopwatch...")
    start_time = time.time()  
    
    input("Press Enter to stop the stopwatch...")
    end_time = time.time() 
    
    elapsed_time = end_time - start_time 
    
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Run the stopwatch program
stopwatch()
