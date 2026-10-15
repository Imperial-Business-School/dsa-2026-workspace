test = {
  'name': 'test_greedy_heuristic',
  'points': 25,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pl_items, players = read_players('data/fantasy.json')
          >>> team, val = greedy_heuristic(pl_items, 900, density, 11)
          >>> [val, len(team)]
          [357.0, 11]
          >>> team, val = greedy_heuristic(pl_items, 500, density, 11)
          >>> [val, len(team)]
          [289.0, 9]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from greedy import *
      >>> from greedy_extra import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
