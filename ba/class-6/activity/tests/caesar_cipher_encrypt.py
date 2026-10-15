test = {
  'name': 'caesar_cipher_encrypt',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> caesar_cipher_encrypt('a', 1)
          'b'
          >>> caesar_cipher_encrypt('abc', 1)
          'bcd'
          >>> caesar_cipher_encrypt('abc', 4)
          'efg'
          >>> caesar_cipher_encrypt('thisistherealdeal', 6)
          'znoyoyznkxkgrjkgr'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from structs_files_errors_extra import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
