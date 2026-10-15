test = {
  'name': 'broken_factorial',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> broken_factorial(0)
          1
          >>> broken_factorial(1)
          1
          >>> broken_factorial(2)
          2
          >>> broken_factorial(3)
          6
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from seq_data import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
