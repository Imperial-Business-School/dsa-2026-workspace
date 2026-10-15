test = {
  'name': 'Dictionaries',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> d1 = dict() # If there's an error, type Error
          >>> d1['Penny'] = 'penny[at]hotmail.com'
          >>> print(d1['Penny'])
          111b1b8ae9f63fb4dffde512a77bbfe6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # If there's an error, type Error
          >>> d1 = dict(Mateo='mateo[at]imperial.ac.uk')
          >>> d1['Dave'] = 'dave93[at]gmail.com'
          >>> print(d1['Mateo'])
          27afd950e028928285d6dc001d87e68f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # If there's an error, type Error
          >>> songs = {'Kraftwerk': 'Trans-Europe Express', 'Talking Heads': 'I Zimbra'}
          >>> songs['Steve Reich'] = 'Electric Counterpoint'
          >>> songs['Talking Heads'] 
          d761fd7b6c7de3e80e9160b6ae9b399f
          # locked
          >>> 'Electric Counterpoint' in list(songs)
          6f112e0776e191b5e4dfb1ceb0fd2e17
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> d = {'Joe':123, 'Jane':234}
          >>> sorted(list(d.keys()))
          4eac215d05ad7a686aad43daf7d6a558
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
