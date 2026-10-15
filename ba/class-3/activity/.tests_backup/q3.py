test = {
  'name': 'Lists',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> l1 = [17, 'a', 2, 'tokyo']
          >>> len(l1)
          8f12a88870c58b43f43e9d2d1ebc2f63
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [17, 'a', 2, 'tokyo']
          >>> l2 = ['g', 3, 'k']
          >>> len(l1) + len(l2)
          63eedd02149d2d2355514cd055b2d784
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [17, 'a', 2, 'tokyo']
          >>> l1[2] 
          904eef8e72d1fc3b59bf279bc0e834b2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [17, 'a', 2, 'tokyo']
          >>> l1[1:3] # in case of list, write in the following format: [a, b, c, d, e, f]
          944486212dd5376a72951f0b536abfbb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [1, 5, 3]
          >>> for number in l1:
          ...     print(number**2)
          d7b8f7bd8922caf9bcf430c46497c748
          88ee06fb07e8c119cc58f5534c621aa6
          f289c5b9255c9831c684e7945bad4fe3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # If there is an error, type Error
          >>> visited_cities = [['Paris', 'France'], ['Berlin', 'Germany'], ['Bucharest', 'Romania']]
          >>> print(visited_cities[0])
          d0656f06644636a51ed772f88c2ec2ca
          # locked
          >>> print(visited_cities[2][1])
          ab49252f72f91da84f85aceba5bba68a
          # locked
          >>> print(visited_cities[2][2])
          5361ba62bf27fb50a5a321bbb5efd5a3
          # locked
          >>> for pair in visited_cities:
          ...     print(pair[1])
          550b2e71e444d1cb11366597a541e245
          228e1e249e228fda2e77411851a46f80
          ab49252f72f91da84f85aceba5bba68a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # country and its population in millions
          >>> countries = [['France', 65], ['Germany', 80], ['Italy', 60]]
          >>> pop_sum = 0
          >>> for item in countries:
          ...     pop_sum += item[1]
          ...     print(pop_sum)
          199879a0e1e3a5c0165931fe7bf4e56e
          dd62d1acc28b3ac7c40fd3669a2ff4d5
          6cc03ae062e536566de4a994b3cf568b
          # locked
          >>> for item in countries:
          ...     item[1] += 1
          >>> print(countries[1][1])
          873acc66f862ca6289a2842c0971a47e
          # locked
          >>> populations = []
          >>> for item in countries:
          ...     populations.append(item[1])
          >>> print(populations)
          c9017f8ad5d1123ecc49dbc901dec9da
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
