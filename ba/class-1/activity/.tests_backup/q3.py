test = {
  'name': 'Strings',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = 'Franz'
          >>> y = 'Kafka'
          >>> z = x + y
          >>> print(z)
          404d15632d1e231ed61e685ede57257c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = 'Franz'
          >>> y = 'Kafka'
          >>> c = ' '
          >>> z = x + c + y
          >>> print(z)
          6779a6280102444565202ba174c4e5b0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print('Two'*1 + 'Three'*2)
          810386b9a34532d97096fc2b1924f4ef
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> phrase = 'It wasn\'t me' # If the code results in an error, type Error
          >>> print(phrase)
          c79194962d00385f1bd905f866382dd8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> phrase = 'It wasn't me' # If the code results in an error, type Error
          b393ad58e8c783f552c037c63a48b5a0
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
