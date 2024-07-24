'''

@Author:Naveen Madev Naik
@Date: 2024-07-23 12:57:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2024-07-23 12:57:00
@Title :Program to find the Fewest Notes to be returned from Vending Machine

'''


def calculate_min_notes_recursive(change, denominations):
    """
    Description:
          Recursive function to calculate minimum number of notes needed.
    Parameter:
        change:how much amount needs to given as change
        denominations:its list parameter, that conatins notes (1,2,5,10,50,100,200,500,100) used to give change 
    return:
       dictionary and list         
    """
    if change == 0:
        return {}, []
    
    if not denominations:
        return {}, []

    # Get the current largest denomination
    denomination = denominations[0]
    
    # Initialize the notes_count and notes_list
    notes_count = {}
    notes_list = []
    
    if change >= denomination:
        # Calculate how many notes of the current denomination
        count = change // denomination
        remaining_change = change % denomination
        
        # Recursively calculate for the remaining change and denominations
        sub_notes_count, sub_notes_list = calculate_min_notes_recursive(remaining_change, denominations[1:])
        
        # Update the notes_count and notes_list
        notes_count[denomination] = count
        notes_list = [denomination] * count + sub_notes_list

        # Merge sub_notes_count into notes_count
        for sub_denomination, sub_count in sub_notes_count.items():
            if sub_denomination in notes_count:
                notes_count[sub_denomination] += sub_count
            else:
                notes_count[sub_denomination] = sub_count

    else:
        # If the current denomination is larger than the remaining change, move to next denomination
        return calculate_min_notes_recursive(change, denominations[1:])
    
    return notes_count, notes_list

# Input from the user
def main():
    try:
        amount = int(input("Enter the change amount in Rs: "))
        if amount < 0:
            raise ValueError("change amount must be positive integer")
        else:
            denominations = [1000, 500, 100, 50, 10, 5, 2, 1]
            notes_count, notes_list = calculate_min_notes_recursive(amount, denominations)
            total_notes = sum(notes_count.values())
            print(f"Minimum number of notes needed: {total_notes}")
            print(f"Notes to be returned: {notes_list}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__=='__main__':
    main()
