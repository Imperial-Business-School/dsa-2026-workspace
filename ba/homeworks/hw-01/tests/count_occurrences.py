test = {
  'name': 'count_occurrences',
  'points': 18,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
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
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hw_01 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
