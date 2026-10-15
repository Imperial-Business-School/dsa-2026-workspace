"""

Homework 2

"""

def buy_and_hold(prices, start_index=0, starting_money=100.0):
    """
    Buy and hold strategy

    Parameters:
        prices (list): stock prices
        start_index (positive integer, optional): index from which to start the strategy
        starting_money (float, optional): starting cash position. Defaults to 100.0.

    Returns:
        list containing value of position using buy and hold strategy

    Example use:
    >>> res = buy_and_hold([2.0, 1.5, 1.8, 2.3, 2.5])
    >>> [round(x, 1) for x in res]
    [100.0, 75.0, 90.0, 115.0, 125.0]
    >>> [round(x, 2) for x in buy_and_hold([2.0, 1.5, 1.8, 2.3, 2.5], start_index=2)]
    [100.0, 100.0, 100.0, 127.78, 138.89]
    """
    # Your code here. Don't change anything above.
    pass


def moving_average(prices, n):
    """
    Calculates n-period moving average of a list of floats/integers.

    Parameters:
        prices: list of values (ordered in time),
        n: integer moving-average parameter

    Returns:
        list with None for the first n-1 values in prices and the appropriate moving average for the rest

    Example use:
    >>> ma = moving_average([2,3,4,5,8,5,4,3,2,1], 3)
    >>> [round(m, 2) if m is not None else None for m in ma]
    [None, None, 3.0, 4.0, 5.67, 6.0, 5.67, 4.0, 3.0, 2.0]
    >>> moving_average([2,3,4,5,8,5,4,3,2,1], 2)
    [None, 2.5, 3.5, 4.5, 6.5, 6.5, 4.5, 3.5, 2.5, 1.5]
    """
    # Your code here. Don't change anything above.
    pass


def compare_mas(ma1, ma2):
    """
    Compare two moving averages.

    Compares values in ma1 and ma2 pairwise to create a list of indicators such that
    - If ma1 > ma2, indicator = 1
    - Otherwise indicator = 0
    - The moving averages may contain None-values in the beginning. If either value is None, the indicator is None

    Parameters:
        ma1 (list): moving average (list of prices)
        ma2 (list): moving average (list of prices)

    Returns:
        list: binary indicators for which moving average value is greater

    Example use:
    >>> p1 = [1, 2, 4, 5]
    >>> p2 = [0, 2.5, 5, 3]
    >>> compare_mas(p1, p2)
    [1, 0, 0, 1]
    >>> p1 = [None, 2.5, 3.5, 4.5, 4.5, 3.5, 2.5, 1.5, 3.5, 3.5]
    >>> p2 = [None, None, 3.0, 4.0, 4.33, 4.0, 3.0, 2.0, 3.0, 2.66]
    >>> compare_mas(p1, p2)
    [None, None, 1, 1, 1, 0, 0, 0, 1, 1]
    """
    # Your code here. Don't change anything above.
    pass


def ma_strategy(prices, comparisons, starting_cash=100.0):
    """
    Trade based on moving average crossovers

    Parameters:
        prices: list if stock prices
        comparisons: list of comparisons from compare_mas
        starting_cash (float, optional): Starting cash position, defaults to 100.0.

    Returns:
        list of values of the current position: either cash position or the market value of stock position

    We initially hold cash, and buy when we first get a signal to buy.

    More specifically, a change from value 0 to 1 in comparisons signals there's a crossover in moving averages, so we want to buy stock. A move from 1 to 0 signals that we want to sell stock.

    Whenever we trade, we buy with our entire cash position, or sell our entire stock position.
    We will therefore always hold either stock or cash, but never both.

    Assume we can hold fractional stock quantities, and there are no transaction fees.

    Example use:
    >>> starting_cash = 1.0
    >>> prices = [2,4,6,5,1]
    >>> cos = [0, 1, 1, 0, 0] # not real indicators, just to illustrate portfolio value when trading
    >>> values = ma_strategy(prices, cos, starting_cash)
    >>> values
    [1.0, 1.0, 1.5, 1.25, 1.25]
    >>> starting_cash = 1000.0
    >>> prices = [2,3,4,5,4,3,2,1,6,1,5,7,8,10,7,9]
    >>> cos = [None, None, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0]
    >>> values = ma_strategy(prices, cos, starting_cash)
    >>> [round(v, 2) for v in values] # round every value of the returned list using list comprehension
    [1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 166.67, 833.33, 833.33, 952.38, 1190.48, 833.33, 1071.43]
    """
    # Your code here. Don't change anything above.
    pass


def gallery(visits, option=2):
    """
    Produce summary statistics of gallery visits.

    Parameters:
        visits: list of visits (see also HTML instructions):
            Each visit is a tuple (room number (str), visitor number (str), time (str)) (all elements are integers in string format)
            Each visitor starts outside any room, and they leave all rooms in the end.
            The visits are not necessarily in order.
        option (int, optional): determines what to return, see below

    Returns:
        a list containing tuples for each room (sorted in increasing number by room number (1, 2, 3, ...)):
        - if option = 0, (room number, number of unique visitors)
        - if option = 1, (room number, number of unique visitors, average visit time)
        - if option = 2, (room number, number of unique visitors, average visit time, highest total time spent in the room by a single visitor)
        - the average visit time is rounded to the nearest integer using
          Python's built-in round() function. Note that round() uses
          "round half to even": round(2.5) is 2, not 3, and round(3.5) is
          4, not 3. Use round() directly (do not write your own rounding
          logic) so your output matches the expected results exactly.

    Example use:
    >>> visits = [('0', '0', '20'), ('0', '0', '25'), ('1', '1', '74'), ('1', '1', '2')]
    >>> gallery(visits)
    [('0', 1, 5, 5), ('1', 1, 72, 72)]
    >>> gallery(visits, 0)
    [('0', 1), ('1', 1)]
    >>> gallery(visits, 1)
    [('0', 1, 5), ('1', 1, 72)]
    >>> gallery(visits, 1)[0]
    ('0', 1, 5)
    >>> visits = [('15', '3', '61'), ('15', '3', '45'), ('6', '0', '91'), ('10', '4', '76'), ('6', '0', '86'), ('6', '4', '2'), ('10', '1', '47'), ('6', '3', '17'), ('6', '4', '41'), ('15', '3', '36'), ('6', '2', '97'), ('15', '4', '58'), ('6', '0', '16'), ('10', '2', '21'), ('10', '4', '75'), ('6', '0', '76'), ('15', '4', '50'), ('10', '1', '64'), ('6', '3', '3'), ('15', '3', '35'), ('6', '2', '96'), ('10', '2', '35'), ('10', '2', '77'), ('10', '2', '48')]
    >>> gallery(visits)
    [('6', 4, 24, 65), ('10', 3, 15, 43), ('15', 2, 8, 17)]
    """
    # Your code here. Don't change anything above.
    pass


# Written answer (3 points, graded separately -- only this file is
# submitted, so write your answer here as a comment, not in the notebook):
# what data structure(s) did you use above to aggregate the data, and why?
# What's the time complexity of your solution, in terms of the number of
# visit records?
#
# Your answer:


def max_concurrent(events):
    """
    Finds the maximum number of attendees present in a venue at any single moment.

    An attendee is considered present from their check-in time up to,
    but not including, their check-out time.

    Parameters:
        events: list of (attendee_id, check_in_time, check_out_time) tuples.
            attendee_id is a string; check_in_time and check_out_time are integers,
            with check_in_time < check_out_time. The list is not necessarily sorted.

    Returns:
        integer: the maximum number of attendees present at any single moment

    Your solution should run well below O(n^2) for large numbers of attendees:
    a nested loop comparing every pair of attendees' intervals is not an
    acceptable solution here.

    Example use:
    >>> max_concurrent([('A', 9, 11), ('B', 10, 12), ('C', 11, 13)])
    2
    >>> max_concurrent([('A', 9, 17), ('B', 10, 12), ('C', 10, 11), ('D', 16, 18)])
    3
    >>> max_concurrent([('A', 9, 10), ('B', 10, 11)])
    1
    """
    # Your code here. Don't change anything above.
    pass


# Written answer (7 points, graded separately -- only this file is
# submitted, so write your answer here as a comment, not in the notebook).
# Briefly state:
# - What data structure(s) you used above and why
# - The time complexity of your solution in terms of n (the number of attendees)
# - What the naive O(n^2) approach would look like, and specifically why it's slower
#
# Your answer:


class HashTable:
    """
    A simple hash table using chaining for collision resolution.

    Internally, keeps a fixed-size list of "buckets" (self.buckets). Each
    bucket is a list of (key, value) pairs. A key's bucket is chosen by
    hashing the key and reducing modulo the number of buckets -- see _hash
    below, which is where you'll write your own (simple) hash function.

    Example use:
    >>> ht = HashTable(num_buckets=4)
    >>> ht['AAPL'] = 150
    >>> ht['MSFT'] = 300
    >>> ht['AAPL']
    150
    >>> 'MSFT' in ht
    True
    >>> 'GOOG' in ht
    False
    >>> len(ht)
    2
    >>> ht['AAPL'] = 155
    >>> ht['AAPL']
    155
    >>> len(ht)
    2
    """

    def __init__(self, num_buckets=8):
        """
        Initialises an empty hash table with the given number of buckets.

        This is done for you: self.buckets is a list of num_buckets empty
        lists, and self.count tracks how many key-value pairs are stored
        (you'll need to update this yourself in __setitem__).
        """
        self.num_buckets = num_buckets
        self.buckets = [[] for _ in range(num_buckets)]
        self.count = 0

    def _hash(self, key):
        """
        Returns the bucket index for a given key. You'll write your own
        (simple) hash function here, rather than relying on a library.

        Assume key is always a string (e.g. a stock ticker like 'AAPL').

        Steps:
        1. Turn the key into a number by summing the character codes of
           each of its characters. Python's built-in ord(c) function
           returns the integer code point of a single character c, e.g.
           ord('A') is 65. So the "character sum" of 'AAPL' is
           ord('A') + ord('A') + ord('P') + ord('L') = 65+65+80+76 = 286.
        2. Reduce that number modulo self.num_buckets to get a valid
           bucket index, and return it.
        """
        # Your code here. Don't change anything above.
        pass

    def __setitem__(self, key, value):
        """
        Sets ht[key] = value. If key already exists, its value is updated
        rather than a duplicate entry being added.

        Steps:
        1. Find the right bucket using self._hash(key).
        2. Loop through the (key, value) pairs already in that bucket. If
           you find one with a matching key, replace it with the new
           (key, value) pair and return -- don't fall through to step 3.
        3. If you didn't find an existing entry for this key, append the new
           (key, value) pair to the bucket, and increment self.count.
        """
        # Your code here. Don't change anything above.
        pass

    def __getitem__(self, key):
        """
        Returns the value associated with key.
        Raises KeyError if key is not present (same as a regular dict).

        Steps:
        1. Find the right bucket using self._hash(key).
        2. Loop through the (key, value) pairs in that bucket, looking for
           a matching key. If you find one, return its value.
        3. If you get through the whole bucket without finding the key,
           raise KeyError(key).
        """
        # Your code here. Don't change anything above.
        pass

    def __contains__(self, key):
        """
        Returns True if key is present in the hash table, False otherwise.
        Supports the `key in ht` syntax.

        This should look very similar to __getitem__, but returning
        True/False instead of a value/exception. (You may find it easiest
        to write this one by calling __getitem__ and catching KeyError --
        or by repeating the same bucket search directly. Either is fine.)
        """
        # Your code here. Don't change anything above.
        pass

    def __len__(self):
        """
        Returns the number of key-value pairs stored in the hash table.
        Supports the `len(ht)` syntax.
        """
        # Your code here. Don't change anything above.
        pass


# Written answer 1 (5 points, graded separately -- only this file is
# submitted, so write your answer here as a comment, not in the notebook).
# Your hash function has a systematic
# weakness: give a concrete example of two different keys that produce
# exactly the same hash, not by coincidence but because of how the
# character-sum function is built. Explain why this happens.
#
# Your answer:


# Written answer 2 (5 points, graded separately -- same rule: write it here,
# not in the notebook). After
# implementing HashTable, write a short comparison against a plain list of
# (key, value) pairs searched linearly. Insert an increasing number of items
# (e.g. 100, 1,000, 10,000) into both structures and time how long a batch of
# lookups takes in each. Briefly report what you observe, and explain why,
# in terms of time complexity.
#
# Your answer:
