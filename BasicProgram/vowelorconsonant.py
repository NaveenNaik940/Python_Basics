'''
@Author:Naveen Madev Naik
@Date: 2024-07-22 13:21:00
@Last Modified by: Naveen Madev Naik
@Last Modified time: 2021-02-11 18:00:30
@Title :checking vowel or consonant
'''
def check_vowel_or_consonant(char):
    """
    Description:
         this function will return character is vowel or consonant
    Parameter:
         char: char will be used to check whether its is vowel or consonant
    return:
       string          
    """    
    vowels = 'aeiouAEIOU'
    if char.isalpha() and len(char) == 1:
        if char in vowels:
            return f"'{char}' is a Vowel."
        else:
            return f"'{char}' is a Consonant."
    else:
        return "Invalid input. Please enter a single alphabetic character."


character=input("Enter the Character").lower()
character=character[0]
result = check_vowel_or_consonant(character)
print(result)


