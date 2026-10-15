test = {
  'name': 'count_tweets_by_source',
  'points': 7,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import json
          >>> with open('data/trump_tweets_small.json', encoding='utf8') as f:
          ...     tweets = json.load(f)
          >>> counts = count_tweets_by_source(tweets)
          >>> counts['Twitter for Android']
          12
          >>> counts['Twitter for iPhone']
          7
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from trump_tweets_json import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
