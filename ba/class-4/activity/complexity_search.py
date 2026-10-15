def linear_search_index(A, x):
    """ 
    Searches for element x in list A
    
    Parameters:
        A: list
        x: the element we're searching for.
    
    Returns the first index at which x found, -1 if not found
    
    Example use:
    >>> linear_search_index([1, 3, 9, 4, 5, 6], 6)
    5
    >>> linear_search_index([1, 3, 9, 4, 5, 6], 2)
    -1
    """
    # YOUR CODE HERE
    # DON'T CHANGE ANYTHING ABOVE      


def binary_search_count(A, x):
    """
    Binary search for element x in list A
    
    Parameters:
        A: list with elements in ascending order.
        x: the element we're searching for.
   
    Returns 
        True if x found, False if not found
        the number of iterations taken to find the result
    
    >>> binary_search_count([1, 3, 4, 5], -1)
    (False, 2)
    >>> binary_search_count([1, 3, 4, 5, 6, 6, 7], 5)
    (True, 1)
    """
    # YOUR CODE HERE
    # DON'T CHANGE ANYTHING ABOVE 
    # Initialize the search to cover entire list
    low = 0
    high = len(A) - 1 
    while low <= high:
        midpoint = (low + high) // 2
        guess = A[midpoint]
        if guess == x:
            return True
        elif guess > x:
            high = midpoint - 1 
        else:
            low = midpoint + 1 
    return False

 