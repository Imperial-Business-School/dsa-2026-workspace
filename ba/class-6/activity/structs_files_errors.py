def print_dict_values(a):
    """
    Prints the key-value pairs of the input dictionary a, sorted based on the key value

    Parameters:
        a: dictionary a

    Returns:
        the number of keys the input dictionary includes

    Examples:
    >>> print_dict_values({'Zoe': 'ICL', 'Mark': 'UCL'})
    Mark UCL
    Zoe ICL
    2
    >>> print_dict_values({'banana': 'yellow', 'apple': 'green', 'berry': 'blue'})
    apple green
    banana yellow
    berry blue
    3
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    sorted_keys = sorted(a.keys())
    for key in sorted_keys:
        print(f"{key} {a[key]}")
    return len(a)


def count_characters(a):
    """
    Counts how many times different characters appear in the input string.

    Returns:
        dictionary whose:
            keys are the characters appearing in the input string a
            values are the counts of the characters in the input string a

    Examples:
    >>> count_characters('aaaa')
    {'a': 4}
    >>> x = count_characters('test')
    >>> print(x['t'])
    2
    >>> x = count_characters('hello')
    >>> print(x['h'])
    1
    >>> x = count_characters('hello world')
    >>> print(x['l'])
    3
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    counts = {}
    for char in a:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def divide(a, b):
    """
    Divides a by b; catches division by zero

    Parameters:
        a, b: numbers

    Returns:
        a divided by b.
        If b is 0, prints out 'No division by 0.' and returns None

    Examples
    >>> divide(10, 2)
    5.0
    >>> divide(10, 0)
    No division by 0.
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    if b == 0:
        print("No division by 0.")
        return None
    return a / b

def count_words(a):
    """
    Counts the occurrence of different words in the input string a

    Parameters:
        a: string

    Returns:
        dictionary whose:
            keys are words
            values are the counts of the words in the input string a

    Examples:
    >>> x = count_words('test sentence')
    >>> print(x['test'])
    1
    >>> x = count_words('it is what it is')
    >>> print(x['it'])
    2
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    counts = {}
    words = a.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

