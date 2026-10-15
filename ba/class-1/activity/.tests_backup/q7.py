test = {
  'name': 'While loops',
  'points': 15,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> n = 2
          >>> while n >= 0: # In case of infinite loop, type Infinite loop
          ...     n = n - 1
          ...     print(n)
          cf62fa01f6464ba1123d2feb3e7f3e4a
          c3b4db86c646ae28ec8cf237480def38
          8013af6a430292dadae88fc158c83ec2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> n = 1
          >>> while n >= 0: # In case of infinite loop, type Infinite loop
          ...     n = n + 1
          ...     print(n)
          ea6acf85dc9e993a394ee2e4718c14b0
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
          cf62fa01f6464ba1123d2feb3e7f3e4a
          c3b4db86c646ae28ec8cf237480def38
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
