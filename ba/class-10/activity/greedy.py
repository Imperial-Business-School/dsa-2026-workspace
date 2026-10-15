import random


##########################################
# Building a knapsack of items
# No need to do anything here, but take note
# of what we can do with an 'Item'


class Item(object):
    """
    Knapsack item

    Has a name, a value, and a weight.
    """
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):  # This gets called when we use print() on an item
        result = '<' + self.name + ', ' + str(self.value)\
                 + ', ' + str(self.weight) + '>'
        return result


##########################################
# Helper function to generate random items
# No need to do anything here, but find
# good examples of list comprehensions!

def generate_items(n=10, max_value=100, max_weight=10):
    """
    Generate a list of random items

    Parameters:
        n - number of items
        max_value - maximum value of items
        max_weight -  maximum weight of items

    Returns:
        list of n randomly generated items
    """
    # Generate names, values, weights
    names = ['Item ' + str(i) for i in range(n)]
    values = [random.randint(1, max_value) for _ in range(n)]  # Here _ indicates we don't assign value to a name
    weights = [random.randint(1, max_weight) for _ in range(n)]

    # Create a list of items
    items = [Item(n, v, w) for n, v, w in zip(names, values, weights)]
    return items


items_list = generate_items()


##########################################
# Greedy knapsack

# These functions are used for sorting knapsack items according to max value, min cost, and bang-for-buck
# Complete them as described

def value(item):
    """
    Return the value of the item

    Parameters:
        item - an Item object

    Returns:
        the value of the item
    """
    return ...


def weight_inverse(item):
    """
    Return the inverse of item weights

    Parameters:
        item - an Item object

    Returns:
        the inverse of the item's weight
    """
    return ...


def density(item):
    """
    Return the item's ratio of value to weight

    Parameters:
        item - an Item object

    Returns:
        the ratio of value to weight
    """
    return ...


def greedy(items, max_weight, key_function):
    """
    Greedy knapsack solution

    Parameters:
        items - list of Items
        max_weight - knapsack size
        key_function - function to sort items with

    Returns:
        list with the highest-value set of items fitting the knapsack
        the value of the resulting knapsack
    """

    # Sort items by key function to pick into knapsack
    sorted_items = sorted(items, key=key_function, reverse=True)

    # result is the list of items we picked
    result = []
    total_value = 0.0  # knapsack value
    total_weight = 0.0  # knapsack weight, must be <= max_weight

    # Loop through sorted items
    for index in range(len(sorted_items)):
        cur_item = sorted_items[index]
        if ____:
            # if we can fit the entire item into knapsack, do it, update its weight and value
            # code: add item to knapsack
            # code: update knapsack weight and value
            pass  # replace with your code
    return result, total_value


def test_greedy():
    """
    Tests for greedy algorithm
    >>> names = ['clock', 'painting', 'radio']
    >>> values = [175,90,20]
    >>> weights = [10,9,4]
    >>> items = [Item(n, v, w) for n,v,w in zip(names, values, weights)]
    >>> res, val = greedy(items, 5, density)
    >>> [val, len(res)]
    [20.0, 1]
    >>> res, val = greedy(items, 13, density)
    >>> [val, len(res)]
    [175.0, 1]
    >>> res, val = greedy(items, 13, weight_inverse)
    >>> [val, len(res)]
    [110.0, 2]
    """
    # Please do not edit this function
    pass

##########################################
# Brute force version


def power_set(a_list):
    """
    Generator that creates all subsets of input list
    """
    if len(a_list) <= 1:
        yield a_list  # Google what this does!
        yield []
    else:
        for item in power_set(a_list[1:]):
            yield [a_list[0]] + item
            yield item


def brute_force(items, max_weight):
    """
    Brute-force knapsack solution

    Parameters:
        items - list of Items
        max_weight - knapsack size

    Returns:
        list with the highest-value set of items fitting the knapsack
        the value of the resulting knapsack

    """
    best_val = 0.0
    best_set = None
    pset = power_set(items)
    # Loop through all subsets
    for item_set in pset:
        kn_val = 0.0
        kn_weight = 0.0
        for kn_item in item_set:  # add all items to knapsack
            kn_val += kn_item.get_value()
            kn_weight += kn_item.get_weight()
        if kn_weight <= max_weight and kn_val > best_val:  # best solution and a feasible solution?
            best_val = kn_val
            best_set = item_set
    return best_set, best_val


##########################################
# Dynamic programming version


def knapsack_dp(items, max_weight):
    """
    Exact (optimal) solution to the binary knapsack problem, using
    dynamic programming: recursion with memoization.

    Assumes max_weight and every item's weight are whole numbers, so
    that remaining capacity can be used as an index into the memo.

    Parameters:
        items - list of Items
        max_weight - knapsack size (a whole number)

    Returns:
        the value of the best possible knapsack (float)

    This uses the same recursive idea we learned in Class 5, plus one
    new idea: memoization.

    Define best(i, w) = the best value achievable using only items[i:],
    with remaining capacity w. Then:
    - Base case: if i == len(items), there are no items left to
      consider, so best(i, w) = 0.
    - Recursive case: look at items[i].
        - If it doesn't fit (its weight > w), we have no choice but to
          skip it: best(i, w) = best(i + 1, w).
        - If it does fit, we have two options, and should take
          whichever is better:
            - skip it: best(i + 1, w)
            - take it: its value + best(i + 1, w - its weight)
          best(i, w) = max(skip, take)

    Without memoization, this recursion recomputes the same (i, w)
    pair many times over (there are many different sequences of
    choices that lead to the same "items left, capacity left" state) --
    that's exactly what makes plain brute-force recursion exponential.
    Memoization -- caching each (i, w) result the first time it's
    computed, and reusing it after that -- is what turns this into
    dynamic programming: there are only len(items) * (max_weight + 1)
    distinct (i, w) pairs, so the whole computation takes that much
    time instead.
    """
    memo = {}

    def best(i, w):
        if (i, w) in memo:
            return memo[(i, w)]

        if i == len(items):
            result = 0.0
        else:
            # YOUR CODE BELOW
            # Hint: look at items[i]. If it doesn't fit in remaining
            # capacity w, skip it. Otherwise, compare skipping it to
            # taking it, and keep the better of the two.
            pass

        memo[(i, w)] = result
        return result

    return best(0, int(max_weight))


def test_knapsack_dp():
    """
    Tests for dynamic programming knapsack solution
    >>> names = ['gold', 'silver', 'bronze']
    >>> values = [60, 100, 120]
    >>> weights = [10, 20, 30]
    >>> items = [Item(n, v, w) for n, v, w in zip(names, values, weights)]
    >>> knapsack_dp(items, 50)
    220.0
    >>> names = ['clock', 'painting', 'radio']
    >>> values = [175, 90, 20]
    >>> weights = [10, 9, 4]
    >>> items = [Item(n, v, w) for n, v, w in zip(names, values, weights)]
    >>> knapsack_dp(items, 13)
    175.0
    >>> knapsack_dp(items, 5)
    20.0
    """
    # Please do not edit this function
    pass
