test = {
  'name': 'is_palindrome',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> is_palindrome('neveroddoreven')
          True
          >>> is_palindrome(to_chars('A man, a plan, a canal: Panama.'))
          True
          >>> is_palindrome('hello')
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from seq_data_extra import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
