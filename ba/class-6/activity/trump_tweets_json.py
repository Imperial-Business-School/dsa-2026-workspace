## Question 9: Trump tweets, JSON edition

# Earlier in the session (and back in Session 3), we worked with a CSV file
# of tweets, where each row was a flat list of values. Real-world data often
# comes in a richer format instead: JSON (JavaScript Object Notation), which
# maps naturally onto Python's own dictionaries and lists. This file works
# with the same tweets dataset, but as JSON: `data/trump_tweets_small.json`
# contains a list of dictionaries, one per tweet, each with the keys
# 'source', 'text', and 'retweet_count'.
#
# You can load it like this:
#
# >>> import json
# >>> with open('data/trump_tweets_small.json', encoding='utf8') as f:
# ...     tweets = json.load(f)
#
# `tweets` is now a list of dictionaries, eg:
# >>> tweets[0]
# {'source': 'Twitter for Android', 'text': '...', 'retweet_count': 3832}


def count_tweets_by_source(tweets):
    """
    Counts how many tweets came from each source.

    Parameters:
        tweets: list of tweet dictionaries, each with a 'source' key

    Returns:
        a dictionary mapping each source (str) to the number of tweets
        from that source (int)

    Example use:
    >>> import json
    >>> with open('data/trump_tweets_small.json', encoding='utf8') as f:
    ...     tweets = json.load(f)
    >>> counts = count_tweets_by_source(tweets)
    >>> counts['Twitter for Android']
    12
    >>> counts['Twitter for iPhone']
    7
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    counts = {}
    
    for tweet in tweets:
        source = tweet['source']
    
        if source in counts:
            counts[source] += 1
    
        else:
            counts[source] = 1
    
    return counts

def tweets_containing(tweets, word):
    """
    Finds the text of every tweet that mentions the given word.

    Parameters:
        tweets: list of tweet dictionaries, each with a 'text' key
        word: str, the word to search for (case-insensitive)

    Returns:
        a list of the 'text' of every tweet containing word, in the same
        order as tweets

    Example use:
    >>> import json
    >>> with open('data/trump_tweets_small.json', encoding='utf8') as f:
    ...     tweets = json.load(f)
    >>> len(tweets_containing(tweets, 'Hillary'))
    4
    >>> tweets_containing(tweets, 'thisworddoesnotappear')
    []
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    matching_tweets = []
    
    target_word = word.lower()
    
    for tweet in tweets:
        if target_word in tweet['text'].lower():
            matching_tweets.append(tweet['text'])
    
    return matching_tweets

def most_retweeted(tweets):
    """
    Finds the text of the single most-retweeted tweet.

    Parameters:
        tweets: list of tweet dictionaries, each with 'text' and
            'retweet_count' keys

    Returns:
        the 'text' (str) of the tweet with the highest 'retweet_count'

    Example use:
    >>> import json
    >>> with open('data/trump_tweets_small.json', encoding='utf8') as f:
    ...     tweets = json.load(f)
    >>> most_retweeted(tweets)[:9]
    'Praying f'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if not tweets:
        return None

    top_tweet = tweets[0]
    
    for tweet in tweets:
        if tweet['retweet_count'] > top_tweet['retweet_count']:
            top_tweet = tweet
            
    return top_tweet['text']