
## Questions 7 - 8

import csv

def read_trump_tweets(file_name):
    """
    Reads Trump tweets csv file into a list
    
    Parameter:
        file_name: csv file containing the tweets
    
    Returns:
        list containing tweets
    """
    try:
        with open(file_name, encoding="utf8") as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            tweet_list = list(data)
        return tweet_list
    except FileNotFoundError:
        print("""
              File not found. Check that the working directory is correct.
              Change the working directory by clicking on folder icon in the top right part of the window.
              """)


## Question 7

def str_to_int(L, ind):
    """
    Convert string-form integer entries in L to integers. 
    
    Parameters:
        L is a list containing list entries. The first entry contains headers so it is skipped.
        ind is the index at each of the list entries to be converted
        
    Returns a new list with integer entries of the ind entry of each entry of L
    
    Example use:
    >>> L = [['Name', 'Favorites'], ['Jay', '100'], ['Jack', '99']]
    >>> y = str_to_int(L, 1)
    >>> print(y)
    [100, 99]
    >>> L = [['Number1', 'Number2'], ['8', '3'], ['7', '5']]
    >>> y = str_to_int(L, 0)
    >>> print(y)
    [8, 7]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW


def value_at_least(L, threshold):
    """
    Collects indices of L where value is at least threshold
    
    Parameters:
        L: a list 
        threshold: value threshold
    
    Returns a new list of indices with values at least the threshold
    
    Example use:
    >>> tw = [0, 100, 3]
    >>> value_at_least(tw, 2)
    [1, 2]
    >>> value_at_least([4, 1, 5], 5)
    [2]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW


## More on tweets
# Applying functions


def apply_function(a_list, function, start_from):
    """
    Applies parameter function to items of a_list. 
    
    Parameters:
        a_list: a list of lists
        function: a function to be applied to each item of a_list,
        start_from: index of a_list to start from
    
    Returns: 
        a new list with the results.
    """
    new_list = []
    for item in a_list[start_from:]:
        new_list.append(function(item))
    return new_list

## Question 8

def count_capital_letters(tweet):
    """
    Counts the number of capital numbers of the tweet
    
    Parameters:
        tweet: list containing tweet text in first item
    
    Returns: 
        integer count of the number of capital letters in the tweet text
    
    Example use:
    >>> count_capital_letters(['HEY YOU', 'date1', 100, 10, 'id'])
    6
    >>> count_capital_letters(['hey YOU', 'date1', 100, 10, 'id'])
    3
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    
def to_chars(s):
    """
    Strips the string s from any non-letter characters (English alphabet), 
    and makes it lower-case.
    
    Parameters:
        string s
    Returns: 
        string with only lower-case chars of the English alphabet
        
    Example use
    >>> to_chars('HeLlo!')
    'hello'
    >>> to_chars("Never (1) odd or (2) even...")
    'neveroddoreven'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    alphabet = 'abcdefghjiklmnopqrstuvwxyz' # English alphabet


def is_palindrome(s):
    """ 
    Palindrome checker
    
    Parameters:
        s is string that has gone through to_chars()
    
    Returns True if s is palindrome, False otherwise
    
    Examples:
    >>> is_palindrome('neveroddoreven')
    True
    >>> is_palindrome(to_chars('A man, a plan, a canal: Panama.'))
    True
    >>> is_palindrome('hello')
    False
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS


def search_word(s1, s2):
    """
    Finds the longest substring of s1 that is also in s2
    
    Parameters: 
        s1, s2 - strings
    
    Returns: 
        the longest substring of s1 also contained in s2
   
    Examples:
    >>> search_word("searching for a substring", "subway")
    'sub'
    >>> search_word("dog owner", "catdog oh catdog")
    'dog o'
    >>> search_word("fish", "filet")
    'fi'
    >>> search_word("fish", "ballet")
    ''
    >>> search_word("land a plane", "lane")
    'lane'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS