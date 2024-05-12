""" Implementation of the Fraction class """

# Imports 
from __future__ import annotations
from typing import Any 
from typing_extensions import Self

# Helper Functions
def gcd(m:int, n:int) -> int :
    
    """
    This is the implementation of the Greatest Common Divisor
    Algorithm that is Euclid's Algorithm. 

    Working: It states that the greatest common divisor of 
    two integers m and n is n if n divides m evenly. 
    However, if n does not divide m evenly, then the answer 
    is the greatest Common divisor of n and the remainder of
    m divided by n. 
    """
    while m%n != 0: 
        m, n = n , m%n 
    return n

# Main class Implementation of Fractions 
class Fraction: 
    """Class Fraction """ 
    def __init__(self, top, bottom) ->None:
        # Constructor Definition
        self.num = top 
        self.den = bottom 

    def __str__(self:Self) -> str : 
        return f"{self.num}/{self.den}" 
    
    def __add__(self:Self, otherfraction:Fraction) -> Fraction:
        new_num = self.num*otherfraction.den + \
                    self.den* otherfraction.num
        new_den = self.den*otherfraction.den 
        common:int = gcd(new_num, new_den)
        return Fraction(new_num//common , new_den//common)  

    def __eq__(self, other_fraction: Fraction) -> bool:
        # We wanted to over ride the equality from shallow to deep 
        # shallow Equality -> Same reference to memory 
        # deep Equality -> Different reference but same data 
        first_num: int = self.num* other_fraction.den 
        second_num: int = other_fraction.num*self.den 
        return first_num == second_num
    
    def __le__(self, other_fraction: Fraction) -> bool :
        # this method overides the less than or equal to method
        first:float = self.num/self.den 
        second:float= other_fraction.num/other_fraction.den 
        if(first<=second): return True 
        return False
    
    def __mul__(self, other_fraction:Fraction) -> Fraction : 
        # Function to implement object multiplication
        num:int = self.num*other_fraction.num 
        den:int = self.den*other_fraction.den 
        common:int = gcd(num, den)
        return Fraction(num//common, den//common)
    
    def __truediv__(self, other_fraction:Fraction)-> Fraction:
        # This overrides the division operator
        num:int = self.num*other_fraction.den 
        den:int = self.den*other_fraction.num
        common:int = gcd(num, den)
        return Fraction(num//common, den//common)
    
    def show(self) -> None: 
        print(f"{self.num}/{self.den}")
        return None 
    
# driver code 
if __name__ == "__main__" :
    # Fraction Set 1
    f1:Fraction = Fraction(1, 4)
    f2:Fraction = Fraction(1, 2)

    # Fraction Set 2
    f3:Fraction = Fraction(1, 2)
    f4:Fraction = Fraction(1, 3)

    # Verbose
    print(f"Sum of the Fractions: {f1+f2}")
    print(f"Comparison: {f3>=f4}") 
    print(f"Multiplication: {f3*f4*f1*f2}")
    print(f"Division: {f3/f2}")
     
