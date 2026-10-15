test = {
  'name': 'caesar_cipher_decrypt',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> caesar_cipher_decrypt('b', 1)
          'a'
          >>> caesar_cipher_decrypt('bcd', 1)
          'abc'
          >>> caesar_cipher_decrypt('efg', 4)
          'abc'
          >>> caesar_cipher_decrypt('znoyoyznkxkgrjkgr', 6)
          'thisistherealdeal'
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
