# -*- coding: utf-8 -*-
"""
Homework 1

Please do not import any Python libraries to solve any of the problems.
"""

#####
# Wind chill calculator
#####


def wind_chill(temp, wind_speed, a=13.12, b=0.6215, c=-11.37, d=0.16, e=0.3965):
    """
    Converts temperature and wind speed into wind-chill index.

    Formula: wci = a + b*T + c*W^d + e*T*W^d, where T is temperature and W is wind speed

    Parameters:
        temp: temperature in Celsius
        wind_speed: wind speed in km/h

        The following constants have default values specified above.
        You don't need to include them in function calls.

        a: constant with default value
        b: constant with default value
        c: constant with default value
        d: constant with default value
        e: constant with default value

    Returns:
        Wind chill index.
        If wind speed is lower than 5, return the temperature.
        Otherwise, return the index according to the formula, rounded to integer value

    Example use:
    >>> wind_chill(10, 0)
    10
    >>> wind_chill(-10, 20)
    -18
    >>> wind_chill(-20, 30) + 1
    -32
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if wind_speed < 5:
        return temp
    else:
        wci = a + b*temp + c*(wind_speed**d) + e*temp*(wind_speed**d)
        return round(wci)
#####
# A brainteaser
#####


def the_35_teaser(n):
    """
    A typical coding interview brainteaser.

    Parameters:
        n: (positive) integer

    Returns:
        - For n divisible by both 3 and 5, return '35'; otherwise:
        - For n divisible by 3, return '3'
        - For n divisible by 5, return '5'
        - Otherwise, return None.

    Example use:
    >>> the_35_teaser(9)
    '3'
    >>> the_35_teaser(95)
    '5'
    >>> the_35_teaser(300)
    '35'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if n%3 == 0 and n%5 == 0:
        return '35'
    
    elif n % 3 == 0:
        return '3'
    
    elif n % 5 == 0:
        return '5'
    
    else:
        return None


def the_35_looper(n):
    """
    Prints the first n values of the_35_teaser starting from 1

    Note you may call the function the_35_teaser

    Parameters:
        n: (positive) integer

    Example use:
    >>> the_35_looper(15)
    None
    None
    3
    None
    5
    3
    None
    None
    3
    5
    None
    3
    None
    None
    35
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    for i in range(1,n+1):
        print(the_35_teaser(i))
    


#####
# Date string conversion: slash-date format to dash-date format
#####


def date_conversion(date_string):
    """
    Converts date string from "US slash format" to "scientific dash format" as specified in the HW instructions.

    Assume input is in American date ordering (month-day-year) -> convert to European ordering (day-month-year).
    Assume that the year of the date is in either range 00 - 99 or 1000 - 9999.

    A two-digit year YY should be interpreted as whichever of YY+1900 or
    YY+2000 falls within the range 1925-2024 (there is always exactly one
    match, since that range is exactly 100 years wide). For example, 16
    becomes 2016 (since 1916 is outside 1925-2024), but 25 becomes 1925
    (since 2025 is outside 1925-2024, but 1925 is exactly at the edge of
    the range). Do NOT just always add 1900 -- check both examples below
    carefully, they use different centuries.

    Parameters:
        date_string: string date in "US slash format", eg, 12/8/16, 1/12/1898, 1/1/25 (we assume valid dates)

    Returns:
        string date in "scientific dash format", eg, 08-12-2016, 12-01-1898, 01-01-1925

    Example use:
    >>> print(date_conversion('12/8/16'))
    08-12-2016
    >>> print(date_conversion('01/12/1898'))
    12-01-1898
    >>> print(date_conversion('11/5/25'))
    05-11-1925
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW

    month_str, day_str, year_str = date_string.split('/')  # Use this to split slash format string into a list

    day = f"{int(day_str):02d}"
    month = f"{int(month_str):02d}"
    
    year_num = int(year_str)
    if year_num < 100:
        if year_num + 1900 >= 1925:
            year = year_num + 1900
        else:
            year = year_num + 2000
    else:
        year = year_num
        
    return f"{day}-{month}-{year}"

#####
# Leap years
#####


def is_leap_year(year):
    """
    Returns True if year is a leap year, False otherwise.

    A year is a leap year if it is divisible by 4, EXCEPT that century
    years (divisible by 100) are only leap years if they are also
    divisible by 400.

    Parameters:
        year: positive integer

    Example use:
    >>> is_leap_year(2024)
    True
    >>> is_leap_year(2023)
    False
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(2000)
    True
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

#####
# Robust version of date conversion
#####


def date_conversion_robust(date_string):
    """
    Converts date string from "US slash format" to "scientific dash format",
    handling invalid input gracefully instead of assuming it is always valid.

    Valid dates are as follows:
    - US date ordering (month-day-year).
    - Two-digit years are in the past century (1925-2024 is "past century", before or after is not).
    - The year of the date is in either range 00 - 99 or 1000 - 9999.
    - An actual date that has occurred or will occur (e.g. no 30th of February,
      and the 29th of February is only valid in leap years -- use is_leap_year).

    Your function must handle each of the following cases. These are the
    only cases you need to consider -- there is no hidden, additional
    invalid input beyond what is described here:

    1. date_string is not a string at all (e.g. an integer). Print
       "Not a valid date." and return None.
    2. date_string does not split (on '/') into exactly 3 parts, or one of
       the parts is not made up of digits (so int() would fail on it).
       Print "Not a valid date." and return None.
    3. The parts are numeric, but the resulting date does not exist as a
       real calendar date in month/day/year order (wrong day-of-month for
       that month, invalid month, or year out of the allowed range) --
       AND swapping the day and month parts *would* produce a valid date.
       In this case, print a message asking the user if they meant to
       swap day and month order (see example below), and return None.
    4. The parts are numeric, but the resulting date is not a real
       calendar date in month/day/year order, and swapping day and month
       would *not* fix it either. Print "Not a valid date." and return None.
    5. Otherwise, the input is valid: return the converted string in dash
       format, exactly as date_conversion does (you may call
       date_conversion to avoid repeating that logic).

    Parameters:
        date_string: should be a string date in "US slash format", eg,
            12/8/16, 1/12/1898, 1/1/25 -- but may not be (see above)

    Returns:
        if input is valid: string date in "dash" format, eg, 08-12-2016, 12-01-1898, 01-01-1925
        otherwise: prints a message as described above, and returns None

    Example use:
    >>> print(date_conversion_robust('12/8/16'))
    08-12-2016
    >>> print(date_conversion_robust('1/12/1898'))
    12-01-1898
    >>> date_conversion_robust('1/1/25')
    '01-01-1925'
    >>> print(date_conversion_robust('16/3/2021'))
    Not a valid date. Did you mean to input 3/16/2021?
    None
    >>> print(date_conversion_robust('2/29/2017'))
    Not a valid date.
    None
    >>> print(date_conversion_robust('131/2/1928'))
    Not a valid date.
    None
    >>> print(date_conversion_robust(2))
    Not a valid date.
    None
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW

    # You can call date_conversion and is_leap_year if you'd like.
def is_valid_date(m, d, y):
    if y < 100:
        full_year = y + 1900 if y + 1900 >= 1925 else y + 2000
    else:
        full_year = y

    if not (1000 <= full_year <= 9999):
        return False

    if m < 1 or m > 12:
        return False

    days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if m == 2 and is_leap_year(full_year):
        max_days = 29
    else:
        max_days = days_in_months[m]

    return 1 <= d <= max_days


def date_conversion_robust(date_string):
    if not isinstance(date_string, str):
        print("Not a valid date.")
        return None

    parts = date_string.split("/")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        print("Not a valid date.")
        return None

    m, d, y = int(parts[0]), int(parts[1]), int(parts[2])

    if is_valid_date(m, d, y):
        return date_conversion(date_string)

    if is_valid_date(d, m, y):
        print(f"Not a valid date. Did you mean to input {d}/{m}/{y}?")
        return None

    print("Not a valid date.")
    return None



#####
# Arbitrary sorting
#####


def comparison_function(value):
    """
    Comparison function for counting_sort

    Parameter:
        value - integer

    Returns:
        ??? such that comparisons of return values work as described

    Example use:
    >>> comparison_function(99) > comparison_function(18783479)
    True
    >>> comparison_function(123) > comparison_function(321)
    False
    >>> comparison_function(1789) > comparison_function(96861)
    True
    """
    s = str(value)
    counts = []

    for digit in "9876543210":
        digit_count = 0
        for char in s:
            if char == digit:
                digit_count += 1
        counts.append(digit_count)

    counts.append(value)
    return tuple(counts)

def counting_sort(items):
    """
    Sorts a list of integers by counting different digits.

    Parameters:
        items - list of positive integers

    Returns:
        sorted copy of items

    Example use:
    >>> counting_sort([98, 19, 29, 41, 9999, 73, 241, 1111, 53, 3, 333])
    [1111, 3, 333, 41, 241, 53, 73, 19, 29, 98, 9999]
    >>> counting_sort([999, 19, 919, 111, 119, 1199, 911])
    [111, 19, 119, 911, 919, 1199, 999]
    >>> counting_sort([1234, 4321, 3214, 2413])
    [1234, 2413, 3214, 4321]
    """
    # Please do NOT edit this function.
    return sorted(items, key=comparison_function)


#####
# Further exercise: recursion on nested structures
#####


def count_occurrences(playlist, target):
    """
    Counts how many times target appears in a (possibly nested) playlist.

    A playlist is either:
    - a single song title (a string), or
    - a list containing songs and/or other (nested) playlists.

    Parameters:
        playlist: a song title (str), or a list of songs/nested playlists
        target: a song title (str) to count occurrences of

    Returns:
        integer: number of times target appears anywhere in playlist,
        at any level of nesting

    This is a recursive function. Think about it in two parts:
    - Base case: if playlist is just a single song (a string), there's
      nothing to recurse into -- just check whether it matches target.
    - Recursive case: if playlist is a list, go through each item and
      call count_occurrences again on that item, adding up the results.
      Each item might itself be a song or another nested playlist --
      the recursive call handles either case for you.

    Example use:
    >>> mixtape = [
    ...     ["Song A", "Song B", "Song C"],
    ...     ["Song D", ["Song A", "Song E"]],
    ...     "Song A",
    ...     "Song F",
    ... ]
    >>> count_occurrences(mixtape, "Song A")
    3
    >>> count_occurrences(mixtape, "Song F")
    1
    >>> count_occurrences(mixtape, "Song Z")
    0
    """
    # Your code here.
    if type(playlist) is str:
        if playlist == target:
            return 1
        return 0

    count = 0
    for item in playlist:
        count += count_occurrences(item, target)
    return count



def total_duration(playlist):
    """
    Returns the total duration (in seconds) of a (possibly nested) playlist.

    A playlist is either:
    - a single song's duration in seconds (an int or float), or
    - a list containing durations and/or other (nested) playlists.

    Parameters:
        playlist: a duration (int/float), or a list of durations/nested playlists

    Returns:
        int/float: total duration in seconds, summed over every song at
        every level of nesting

    Uses the same recursive pattern as count_occurrences: a number is the
    base case (nothing to recurse into), a list is the recursive case
    (add up the total_duration of each item).

    Example use:
    >>> mixtape_durations = [
    ...     [180, 210, 195],
    ...     [220, [175, 205]],
    ...     240,
    ... ]
    >>> total_duration(mixtape_durations)
    1425
    """
    # Your code here.
    if type(playlist) in (int, float):
        return playlist

    total = 0
    for item in playlist:
        total += total_duration(item)
    return total
