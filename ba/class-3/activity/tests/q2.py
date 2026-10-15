test = {
  'name': 'For loops',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> temp = 0
          >>> for i in range(5):
          ...     temp += 2
          >>> print(temp)
          099927c5ca4bdf1df665b749f6535119
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> cnt1 = 0
          >>> cnt2 = 0
          >>> for i in range(2):
          ...     cnt1 += 1
          ...     for j in range(3):
          ...         cnt2 += 1
          >>> print(cnt1, cnt2)
          8b46079f253174c21dd80382e57d59ad
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def loop_fun(n):
          ...     x = n
          ...     for i in range(n):
          ...         y = 0         
          ...         for j in range(n):
          ...             y += x
          ...         x += y
          ...     return x
          >>> loop_fun(2)
          9b0009928af883f16c0c9ddf06968076
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
