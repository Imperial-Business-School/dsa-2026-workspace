test = {
  'name': 'Objects',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type('23')
          981f3af27fba448d56f24e9cec5f7587
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> type(42)
          ffcd8d3b551b3707efca2e1eb16035f0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> number = '3' # If there is an error, type Error
          >>> number = int(number)
          >>> number + 2
          415c792593d6518f6830dfb037e936ba
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> number = '3' # If there is an error, type Error
          >>> type(number * 4)
          981f3af27fba448d56f24e9cec5f7587
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> number = '3' # If there is an error, type Error
          >>> print(number + 2)
          b393ad58e8c783f552c037c63a48b5a0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> c = 5.1 # If there is an error, type Error
          >>> s = str(c)
          >>> print('The number is ' + s)
          a1f6e1c1b5902f7fb5bbc080f504319d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> number = '3' # If there is an error, type Error
          >>> number = float(number * 4)
          >>> number
          ea7072e0e918aea6aa3806961a3453e8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> number = '3'
          >>> number = float(number  + '5')
          >>> number
          b02f6d7e86c8a04de0128b20d28e946f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> int(2.5) + 2.5
          45d631e643397981787aac828ee0b8e7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> max(3, 5.0)
          26ec2332ede5c88790609484131e7fd7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> type(max(3, 1.0))
          ffcd8d3b551b3707efca2e1eb16035f0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> type(max(3, 10.0))
          a2f2d075458934786528f37b36abf6ca
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> round(3.8)
          ec4dd12320cef696c8e66796603713be
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> type(round(4.53))
          ffcd8d3b551b3707efca2e1eb16035f0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> type(round(4.53, 1))
          a2f2d075458934786528f37b36abf6ca
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
