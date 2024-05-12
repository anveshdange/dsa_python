# This python demonstration is to implement a root function 

def sq_root(n:int) -> float:
    """
    This Function uses the Newton's Method or the Newton-Raphson 
    method , named after Issac Newton and Joseph Raphson/ 
    The Newton–Raphson method for approximating square roots
    performs an iterative computation that converges on the 
    correct value. 

    The Equation , new_guess = 0.5* (old_guess + (n/old_guess))
    takes a value n and repeatedly guesses the square root by
    making each new_guess the old_guess in the subsequent
    iteration. The initial guess used here is n/2.

    """

    root: float = n/2 
    k:int 
    for k in range(20): 
        root = 0.5* (root + (n/root)) 
    return root 


if __name__ == "__main__" : 
    p:int = int(input("Give a number: "))
    print(f"The square root of {p} is: {sq_root(p)}")