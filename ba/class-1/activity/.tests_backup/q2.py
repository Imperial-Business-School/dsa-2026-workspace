test = {
  'name': 'Variables',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> a = 5
          >>> b = 6
          >>> c = a * b
          >>> c
          b35ce481a02408703ac38175013a4754
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> z = 1
          >>> b = 5
          >>> z = z + b
          >>> z
          75d018810b439f2474856aaec9ebe436
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> a = 5
          >>> b = 6
          >>> c = a * b
          >>> a = 100
          >>> c
          b35ce481a02408703ac38175013a4754
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> a = 5
          >>> b = 6
          >>> temp = a
          >>> a = b
          >>> b = temp
          >>> print(a)
          >>> print(b)
          75d018810b439f2474856aaec9ebe436
          415c792593d6518f6830dfb037e936ba
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'type': 'wwpp'
    }
  ]
}
