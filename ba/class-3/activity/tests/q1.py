test = {
  'name': 'Recap',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> n = 3
          >>> while n >= 1: # In case of infinite loop, type Infinite loop
          ...     n = n - 1
          ...     print(n)
          904eef8e72d1fc3b59bf279bc0e834b2
          d7b8f7bd8922caf9bcf430c46497c748
          375261e19471b93a4b7bfff6c7b2238f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> n = 0.8
          >>> while n <= 1: # In case of infinite loop, type Infinite loop
          ...     n = n * n
          ...     print(n)
          72eae69a0db448e25437ef3c27f89b4c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def some_function(i):
          ...     if type(i) == str:
          ...         print('A string')
          ...     else:
          ...         print('Something else')
          >>> some_function('Hello there!' + str(float('3.14')))
          2e0d1ac5eb5e5f73a9a8a3e587fc9b8a
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
