test = {
  'name': 'Recap Lists and Dictionaries',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> d = {'dog': 'bone', 'cat': 'mouse', 'bird': 'work', 'cow': 'grass'}
          >>> 'mouse' in d
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> points = {'Maria':[4, 2], 'Tom':[1, 4], 'John':[1, 2]}
          >>> total = []
          >>> for i in points:
          >>>   total.append(sum(points[i]))
          >>> total
          [6, 5, 3]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> a = [3, 6, 8, 2]
          >>> b = ['a','A','er']
          >>> c = a[3::-2]+b[:-1]
          >>> c
          [2, 6, 'a', 'A']
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'type': 'wwpp'
    }
  ]
}
