test = {
  'name': 'most_retweeted',
  'points': 6,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import json
          >>> with open('data/trump_tweets_small.json', encoding='utf8') as f:
          ...     tweets = json.load(f)
          >>> most_retweeted(tweets)[:9]
          'Praying f'
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
