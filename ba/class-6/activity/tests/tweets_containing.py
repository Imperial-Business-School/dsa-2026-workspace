test = {
  'name': 'tweets_containing',
  'points': 7,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import json
          >>> with open('data/trump_tweets_small.json', encoding='utf8') as f:
          ...     tweets = json.load(f)
          >>> len(tweets_containing(tweets, 'Hillary'))
          4
          >>> tweets_containing(tweets, 'thisworddoesnotappear')
          []
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
