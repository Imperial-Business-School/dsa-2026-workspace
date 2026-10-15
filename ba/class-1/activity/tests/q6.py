test = {
  'name': 'Conditional Statements',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = 5 # If there is no output, write Nothing
          >>> if x > 4:
          ...     print('Hey!')
          17e44937ce6b816fd4e3a633b79f2a69
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> dish = 'broccoli' # If there is no output, write Nothing
          >>> if dish == 'potatoes':
          ...     print('My favorite food!')
          >>> else:
          ...     print('Yuck.')
          c357dd78a1432eedba40f03ecb02b40a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> temp = 0 # If there is no output, write Nothing
          >>> if temp >= 30:
          ...     print('Too hot!')
          >>> elif temp <= 0:
          ...     print('Too cold!')
          >>> else:
          ...     print('Perfect!')
          5b2156d79a82194a8328b5075bf9de01
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> temp = 18 # If there is no output, write Nothing
          >>> humidity = 90
          >>> if temp >= 30:
          ...     print('Too hot!')
          ...     if humidity > 80:
          ...         print('I\'m out of here!')
          bf33cf69049bb40b4f17dd01ef037727
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> temp = 40 # If there is no output, write Nothing
          >>> humidity = 90
          >>> if temp >= 30:
          ...     print('Too hot!')
          ...     if humidity > 80 and humidity < 100:
          ...         print('Hot and kind of humid!')
          ...     elif humidity < 80:
          ...         print('Hot but not too humid!')
          ...     else:
          ...         print('I\'m out of here!')
          1016ab47f266245f0851baab8607f860
          d9c4e9d7229d416a9f40037f6b15c02f
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
