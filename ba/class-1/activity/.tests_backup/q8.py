test = {
  'name': 'Session 1 extra',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 8 // 2 * 3 % 5
          16bee1dec38c2be7823c7c24d94d43ba
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> 2 ** 4 // 3 + 2 ** (4 // 3)
          d8862a0408719cc7735e3664db5c3c0c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> price_2015 = 400000
          >>> price_2016 = 500000
          >>> price_pct_change = (price_2016 - price_2015) / price_2015 * 100
          >>> print(price_pct_change)
          46ee69e4306ba60f9d792495c6b8cbaa
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print('I have \n one \n two \n three \n books')
          dacbcb96e75d2a5f1b2d7746bdd40ae1
          27066cfdab46a7ffadc16181b8bd3e5e
          08e3b961441bcd1a4908a4853348c51e
          7f86ed47d890bac43c0d9051d555a4c8
          6fb16e7855511fb6d93e919c742e6641
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> a = '9.95'
          >>> b = float(a)
          >>> type(b)
          a2f2d075458934786528f37b36abf6ca
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> str(int(float(str(1.5))) + 2.5)
          6e0c0e37e6061d2a33946133fea245e3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> float(str(4.2)) + float(int(float(str(4.2))))
          016ac29c30675c9e29895bc75cac2459
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print(1 and not 0 == 5)
          0b83116f73762a3ad398f1db5c594269
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print(0>=0 or 0 and True)
          0b83116f73762a3ad398f1db5c594269
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print(0>=0 and 0 and True)
          c3b4db86c646ae28ec8cf237480def38
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print(5 * 4 == 20, 5 >= 5, not 5 != 4)
          a8cde562b4ce75f6b7929a96262e1246
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> first_name = 'Franz'
          >>> print(first_name == 'Franz', type(first_name) == str)
          1033bd3ad26c3b97bd774a3bfe9bd88e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> ssum, i = 0, 0
          >>> while i < 4:
          >>>     ssum = ssum + i
          >>>     i = i + 1
          >>> print(ssum)
          75d018810b439f2474856aaec9ebe436
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> ssum, i = 0, 0
          >>> while i < 4:
          >>>     i = i + 1  # # caution, we are incrementing before ssum!
          >>>     ssum = ssum + i
          >>> print(ssum)
          05147d18c497d50f410110b689b37c9f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> ssum, i = 0, 0
          >>> while i < 4:
          >>>     if i % 2 == 0:
          >>>         i = i + 2
          >>>     else:
          >>>         i = i + 1
          >>>     ssum = ssum + i
          >>> print(ssum)
          75d018810b439f2474856aaec9ebe436
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> ssum, i = 0, 0
          >>> while i < 84:
          >>>     if i % 2 == 0:
          >>>         i = i + 6
          >>>     else:
          >>>         i = i + 1
          >>>     ssum = ssum + i * (i % 2)
          >>> print(ssum)
          c3b4db86c646ae28ec8cf237480def38
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> ssum, i = 'start:', 0
          >>> while i < 5:
          >>>     i = i + 1
          >>>     ssum = ssum + ' ' + 'i' * i
          >>> print(ssum)
          9f33ae55d3b15a117ed3bf98447974e9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x, sr, cnt = 24, 1, 0
          >>> while abs(sr * sr - x) > 0.1:
          >>>     sr = (sr + x / sr) / 2.0
          >>>     cnt += 1
          >>> print(cnt)
          415c792593d6518f6830dfb037e936ba
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
