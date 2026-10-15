test = {
  'name': 'Comprehensions',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> [x**2 for x in range(2)]
          ef4d198308ddaffdd404c19e521cd735
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> [len(name) for name in ['Joe', 'Mary', 'Zoe']]
          403ef8adde0495d554cc58fbdac2cfca
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> names = {name:len(name) for name in ['John', 'Mary', 'Zoe']}
          >>> names['Zoe']
          dc6e674b400223cea8cbf5f3ce9618c7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> names = [name:len(name) for name in ['John', 'Mary', 'Zoe']]
          >>> names['Zoe']
          a400bf129e1bfa94407e754f6f790095
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> x = {s for s in 'John'}
          >>> 'j' in x
          6f112e0776e191b5e4dfb1ceb0fd2e17
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
