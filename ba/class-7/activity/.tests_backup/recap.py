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
          284955ce13007698ae8d35f81082c68b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> points = {'Maria':[4, 2], 'Tom':[1, 4], 'John':[1, 2]}
          >>> total = []
          >>> for i in points:
          >>>   total.append(sum(points[i]))
          >>> total
          ed1f6a8a546c686b33182502724069fd
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> a = [3, 6, 8, 2]
          >>> b = ['a','A','er']
          >>> c = a[3::-2]+b[:-1]
          >>> c
          af305d3733f60164fefa0c2a4c9c0fcf
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
