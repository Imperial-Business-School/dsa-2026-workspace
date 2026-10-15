test = {
  'name': 'Strings',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> word = 'hello!'
          >>> print(word[1:3])
          3375c67243a39518dc3f2a15fc2cb9ae
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> word = 'hello!'
          >>> len(word)
          4e0285112b680c6b41fbe97375535e30
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> word = 'hElLO!'
          >>> print((word.lower()).capitalize())
          67d6265e244cf28d4c2c93be0fded10d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> word = 'lovely day'
          >>> count = 0
          >>> for letter in word:
          ...     if letter in 'hey':
          ...         count += 1
          >>> print(count)
          3719490cfcb268831669c4136cfdcac8
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
