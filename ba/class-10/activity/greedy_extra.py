# Using Fantasy football data

import json

# This command imports the function greedy from greedy.py
# It will only work if the greedy.py file is in the same directory
from greedy import greedy, Item


##########################################
# Greedy fractional knapsack

def greedy_fractional(items, max_weight, key_function):
    """
    Greedy fractional knapsack solution

    Parameters:
        items - list of Items
        max_weight - knapsack size
        key_function - function to sort items with

    Returns:
        list with the highest-value set of items fitting the knapsack:
            each item of the list should be a tuple (item, fraction_of_item_in_knapsack)
        the value of the resulting knapsack
    """

    # Sort items
    sorted_items = sorted(items, key=key_function, reverse=True)
    result = []  # list of tuples: each item is (item, fraction of the item in knapsack), eg (item,0.8)
    total_value = 0.0  # knapsack value
    total_weight = 0.0  # knapsack weight <= max_weight

    # Loop through all items
    for i in range(len(sorted_items)):
        cur_item = sorted_items[i]
        # If we can fit item into knapsack, do it and update its weight and value
        if ...:
            pass
        else:  # If cannot fit full item, fill knapsack to capacity
            pass
    return result, total_value


def test_greedy_fractional():
    """
    Tests for greedy algorithm
    >>> names = ['clock', 'painting', 'radio']
    >>> values = [175,90,20]
    >>> weights = [10,9,4]
    >>> items = [Item(n, v, w) for n,v,w in zip(names, values, weights)]
    >>> res, val = greedy_fractional(items, 5, density)
    >>> val
    87.5
    >>> res, val = greedy_fractional(items, 13, density)
    >>> val
    205.0
    >>> res, val = greedy_fractional(items, 11, weight_inverse)
    >>> val
    90.0
    """
    # Please do not edit this function
    pass

###########################################
# Player class
# No need to do anything here -- this is very similar to Item, adapted
# for fantasy football players (it also has a team and a position).


class Player(object):
    """
    Player class for knapsack problem

    Has a name, a team, a value, and a weight, position.
    """
    def __init__(self, n, t, v, w, p):
        self.name = n
        self.team = t
        self.position = p
        self.value = int(v)
        self.weight = int(w)

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_position(self):
        return self.position

    def get_weight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + self.position + ', ' + self.team + ', ' + str(self.value) \
                 + ', ' + str(self.weight) + '>'
        return result

    __repr__ = __str__  # nice representation of objects in eg lists


###########################################
# Helper functions
# No need to do anything here -- but going through these later is a
# useful exercise to develop your skills in reading code written by others.


def create_player_list(players, teams):
    """
    Create a list of player objects from list of player data lists
    """
    positions = {1: 'Goalkeeper', 2: 'Defender', 3: 'Midfielder', 4: 'Forward'}

    player_list = []
    for player in players:
        name = f"{player['first_name']} {player['second_name']}"
        team = teams[int(player['team'])]
        weight = int(player['now_cost'])
        value = int(player['total_points'])
        position = positions[int(player['element_type'])]
        player_list.append(Player(name, team, value, int(weight), position))
    return player_list


def read_players(filename):
    """
    Get player data from JSON

    Assumes JSON from the Premier League API https://fantasy.premierleague.com/api/bootstrap-static/

    Could also do directly
    >>> import requests
    >>> r = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    >>> data = r.json()
    """
    with open(filename, 'r') as f:
        data = json.load(f)

    teams = data["teams"]
    team_mapping = {team["id"]: team["name"] for team in teams}
    players = data["elements"]

    # Get players as list
    player_list = create_player_list(players, team_mapping)

    return player_list, players


def value(item):
    """
    Return the value of the item

    Parameters:
        item - an Item object

    Returns:
        the value of the item
    """
    return item.get_value()


def weight_inverse(item):
    """
    Return the inverse of item weights

    Parameters:
        item - an Item object

    Returns:
        the inverse of the item's weight
    """
    return 1/item.get_weight()


def density(item):
    """
    Return the item's ratio of value to weight

    Parameters:
        item - an Item object

    Returns:
        the ratio of value to weight
    """
    return item.get_value() / item.get_weight()


# Try this out for Question 4: load the data, and run the plain greedy
# algorithm on it (no roster constraints yet).
#
# json_data = 'data/fantasy.json'
# pl_items, players = read_players(json_data)
#
# rs, v = greedy(pl_items, 900, density)
# print(v)
# for item in rs:
#    print(item)


##########################################
# Question 6: Greedy heuristic with roster constraints

def greedy_heuristic(items, max_weight, key_function, max_players):
    """
    Greedy knapsack solution with a cardinality constraint (an exact
    number of players) and per-position roster limits: at most 1
    goalkeeper, 4 defenders, 4 midfielders, and 2 forwards.

    The algorithm: sort items by key_function, exactly as in `greedy`.
    Then go through the sorted list once. Pick an item only if all of
    the following hold:
        - adding its weight would not exceed max_weight
        - the team does not already have max_players players
        - the team does not already have the maximum allowed number of
          players in that item's position (goalkeeper/defender/
          midfielder/forward)
    Otherwise, skip it and move to the next item. (Unlike `greedy`,
    fitting under the weight budget is no longer enough on its own --
    you also need to track how many players you've picked in total and
    in each position so far.)

    Parameters:
        items - list of Players
        max_weight - budget constraint
        key_function - function to sort items with
        max_players - maximum total number of players in the team (11)

    Returns:
        list with the team of players picked by the heuristic
        the total value of the resulting team
    """
    # max players allowed for each position
    max_goal = 1
    max_def = 4
    max_mid = 4
    max_fw = 2

    # init: sort items
    sorted_items = sorted(items, key=key_function, reverse=True)
    result = []
    total_value = 0.0  # knapsack value
    total_weight = 0.0  # knapsack weight <= max_weight

    # YOUR CODE BELOW
    # Hint: keep a running count of players picked so far, both in total
    # and separately for each position (goalkeeper/defender/midfielder/
    # forward), and check those counts alongside the weight budget.
    pass
    return result, total_value


def test_greedy_heuristic():
    """
    Tests for the roster-constrained greedy heuristic, using the real
    fantasy football data in fantasy.json.

    >>> pl_items, players = read_players('data/fantasy.json')
    >>> team, val = greedy_heuristic(pl_items, 900, density, 11)
    >>> [val, len(team)]
    [357.0, 11]
    >>> team, val = greedy_heuristic(pl_items, 500, density, 11)
    >>> [val, len(team)]
    [289.0, 9]
    """
    # Please do not edit this function
    pass
