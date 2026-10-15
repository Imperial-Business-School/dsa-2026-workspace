## Question 5

def item_lengths(input_list):
    """
    Create a list containing the lengths of the items in input_list
    
    Parameters:
        input_list: list
    Returns:
        a list containing lengths of items in input_list
    
    Examples:
    >>> item_lengths(['hello', 'how', 'are', 'you', 'doing'])
    [5, 3, 3, 3, 5]
    >>> item_lengths('All happy families are alike'.split())
    [3, 5, 8, 3, 5]
    >>> x = item_lengths('All happy families are alike'.split())
    >>> x[0]
    3
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW


def longest_item(input_list):
    """
    Finds the longest item in input_list
    
    Parameters:
        input_list: list
    Returns:
        the index of the longest item in input_list 
        (if there are ties, return the first such index)
    
    Examples:
    >>> longest_item(['hello', 'how', 'are', 'you'])
    0
    >>> longest_item('All happy families are alike'.split())
    2
    >>> x = longest_item('All happy families are alike'.split())
    >>> isinstance(x, int) # check that result is an integer
    True
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW

## Question 6

def broken_factorial(n):
    """
    Computes the factorial of a given number n.

    Parameters:
        n: int (non-negative integer)

    Returns:
        The factorial of n, calculated as the product of
        all positive integers up to n.

    Examples:
    >>> broken_factorial(0)
    1
    >>> broken_factorial(1)
    1
    >>> broken_factorial(2)
    2
    >>> broken_factorial(3)
    6
    """
    accumulator = 1

    for i in range(1, n):
        accumulator *= i
    
    return accumulator
