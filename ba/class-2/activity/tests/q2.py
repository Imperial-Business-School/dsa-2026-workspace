test = {
  'name': 'Functions',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def mult(x, y):
          ...     product = x * y
          ...     return product
          >>> mult(5,2)
          7bc1af92c3e7befb4cd41f7fc6eb55a3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def some_printing(text):
          ...     if text == 'hey':
          ...         print(text)
          ...     else:
          ...         print('hello')
          >>> some_printing('hi')
          5cd82957fdc0f723ad2c97bdca6ffb50
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def return_one(): # If there is an error, type Error
          ...     return 1
          >>> return_one()
          6bbf77c4f4c29b992b7452b251b86eba
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> return_one() + 1 # return_one works as in the previous case
          d2b32fc9fa05bf74e7c6bd7e3a7ffdf4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> return_one + 1 # If there's an error, type Error
          d3f6a67fafa33466c062dafdcbea2119
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> type(return_one)
          340e32ba47bd0a2a89a78ffc535c7bb8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> type(return_one())
          d8739ff76b14cbb949bfd9e2ca087336
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def print_one(): # If there is an error, type Error
          ...     print(1)
          ...     return 1
          >>> z = print_one()
          >>> print(z)
          6bbf77c4f4c29b992b7452b251b86eba
          6bbf77c4f4c29b992b7452b251b86eba
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def print_one(): # If there is an error, type Error
          ...     print(1)
          ...     return 1
          >>> print(print_one())
          6bbf77c4f4c29b992b7452b251b86eba
          6bbf77c4f4c29b992b7452b251b86eba
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def print_one(): # If there is an error, type Error
          ...     print(1)
          ...     return None
          >>> z = print_one()
          >>> print(z)
          6bbf77c4f4c29b992b7452b251b86eba
          5a9a47fe60704392d8d7d94a2a818bcc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def print_one(): # If there is an error, type Error
          ...     print(1)
          >>> z = print_one()
          >>> print(z)
          6bbf77c4f4c29b992b7452b251b86eba
          5a9a47fe60704392d8d7d94a2a818bcc
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def go(n):
          ...     while n > 0:
          ...         print(n)
          ...         n = n // 2
          >>> go(4)  # If this loops forever, type Infinite Loop.  If it produces an error, write Error. If it displays nothing, write Nothing
          875f61c850489bb83ba79afffd84ec87
          d2b32fc9fa05bf74e7c6bd7e3a7ffdf4
          6bbf77c4f4c29b992b7452b251b86eba
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
