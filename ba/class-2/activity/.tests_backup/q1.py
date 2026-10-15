test = {
  'name': 'Recap',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(4 * 3) # If there is an error, type Error
          65bb2d579064080c04c18cd3c0115d46
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = 2
          >>> y = 3
          >>> x = (y + 1)*x 
          >>> print(x) # If there is an error, type Error
          d3141c32a6183c624135095bd0ca36c3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> temp = 30
          >>> print('Temp: ' + temp) # If there is an error, type Error
          d3f6a67fafa33466c062dafdcbea2119
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
          >>> x = 8
          >>> x < 5
          d23093a9b21750634fea76dab9cc5b29
          # locked
          >>> x > 0 and x < 7
          d23093a9b21750634fea76dab9cc5b29
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> name = 'Franz'
          >>> if name == 'Franz':
          ...     print('Hello ' + name)
          62c0f79ccd3561f19c8526e216427490
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> y = 7
          >>> while y > 0: # In case of infinite loop, type Infinite loop
          ...     y = y // 2
          ...     print(y)
          481c14e7b4fa0619c65417e86cc17f91
          6bbf77c4f4c29b992b7452b251b86eba
          a5164d10af1418a8f3c230569c692e52
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> y = 2
          >>> while y != 0: # In case of infinite loop, type Infinite loop
          ...     y = y // 2
          ...     print(y)
          6bbf77c4f4c29b992b7452b251b86eba
          a5164d10af1418a8f3c230569c692e52
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
