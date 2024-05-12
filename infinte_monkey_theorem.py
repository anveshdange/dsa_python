"""
Infinite Monkey Theorem: 

The theorem states that a monkey hitting
keys at random on a typewriter keyboard 
for an infinite amount of time will almost
surely type a given text, such as the 
complete works of William Shakespeare. 
Well, suppose we replace a monkey with a 
Python function. How long do you think it 
would take for a Python function to 
generate just one sentence of Shakespeare?
The sentence we’ll shoot for is: 
“methinks it is like a weasel” !!

"""

# Imports 
import random
import string 
from typing import List 

# Global variables 
TARGET_STRING:str = "methinks it is like a weasel"

# Function definitions
def rand_string_generator() -> str :
    """ 
    This Function will generate a string that is 28 character 
    long by choosing random letters from the 26 letters in 
    the alphabet plus the space.
    """
    # Get all lowercase and uppercase alphabets from the English language
    lowercase_alphabets:List[str] = list(string.ascii_lowercase)
    # uppercase_alphabets:List[str] = list(string.ascii_uppercase)

    # Combine both lowercase and uppercase alphabets into a single list
    # total_list:List[str] = lowercase_alphabets + uppercase_alphabets
    total_list:List[str] = lowercase_alphabets # removed uppercase
    total_list.append(" ") # added space element in the total list element 

    generated_list: List[str] = list() 
    i:int
    for i in range(1,29) : 
        generated_list.append(random.choice(total_list))
    
    generated_string: str = ''.join(generated_list)

    return generated_string

def str_score(new_string: str) -> bool :
    """ 
    This Function will compare the randomly generated string
    to the actual string to get the exactness

    Parameters:
    new_string: str

    """
    
    for i in range(1, 29):
        if(new_string[i] != TARGET_STRING[i]):
            return False 
    return True

def main() -> None :
    """
    This Function repeatedly calls for generator and compare
    functions and keeps record of the count of this iteration

    """
    while True:
        _COUNT: int = 0 
        #  step1: generate the string 
        new_string:str = rand_string_generator()
        #  step2: compare the string 
        same:bool = str_score(new_string)
        #  step3: If string is same then print the count 
        #         or else increment the count and recurse.
        if same: 
            print(f"Number of Iterations required: {_COUNT}")
            break
        else: _COUNT+=1
    return None
     
        
# Driver code 
if __name__ == "__main__" :
    main()