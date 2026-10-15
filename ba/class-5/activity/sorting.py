def find_min_index(A, k):
    """
    Finds the index of the smallest element in the list A from index k onwards
    
    Parameters:
        A (list)
        k: index from which start search
        
    Example use:
    >>> find_min_index([1, 2, 5, -1], 0)
    3
    >>> find_min_index([1, 1, 1, 5, 9], 2)
    2
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    
    min_index, min_item = min(enumerate(A[k:]),key = lambda x :x[1])
    min_index += k
    return min_index               

def selection_sort(M):
    """
    Sorts the list M using selection sort
    
    Parameters:
        M is a list containing numbers
    
    Returns sorted copy of M.
    
    Uses find_min_index to find index with lowest value
    
    Examples:
    >>> selection_sort([3, 6, 8, 2, 78, 1, 23, 45, 9])
    [1, 2, 3, 6, 8, 9, 23, 45, 78]
    >>> selection_sort([1, 13, -23, 2.7, -3, 5, 7.5])
    [-23, -3, 1, 2.7, 5, 7.5, 13]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    L = M[:] # create a copy of the list to also preserve original list
    n = len(L)
    for index in range(n):
        min_index = find_min_index(L, index)
        # add code to swap elements of L at index and min_index
        if L[min_index] < L[index]:
            L[index], L[min_index] = L[min_index], L[index]
    return L    

def sort_by_key(country_list, key_function):
    """
    Sorts a list of tuples by specified key function, in descending order
    
    Parameters:
        list of tuples; for example: each tuple is (country_name, unemployment, GDP_growth_rate)
        key_function, to be used for sorting
    	
    Returns:
        sorted list of tuples
    Examples: # these are made-up numbers!
    >>> ç
    [('Brazil', 10, 1.7), ('Argentina', 9, 2.3), ('USA', 4.4, 2.3), ('China', 4.1, 9), ('Germany', 4.0, 1), ('Japan', 3.2, 2), ('Thailand', 2, 1.2)]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    return sorted(country_list, key = key_function, reverse = True)

	
def get_unemployment(x):
    """
    Returns the level of unemployment from the parameter x (tuple)
    Parameter: x - tuple (country_name, unemployment, GDP_growth_rate)
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    return x[1]
