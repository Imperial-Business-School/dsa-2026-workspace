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
          penny[at]hotmail.com
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # If there's an error, type Error
          >>> d1 = dict(Mateo='mateo[at]imperial.ac.uk')
          >>> d1['Dave'] = 'dave93[at]gmail.com'
          >>> print(d1['Mateo'])
          mateo[at]imperial.ac.uk
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # If there's an error, type Error
          >>> songs = {'Kraftwerk': 'Trans-Europe Express', 'Talking Heads': 'I Zimbra'}
          >>> songs['Steve Reich'] = 'Electric Counterpoint'
          >>> songs['Talking Heads'] 
          'I Zimbra'
          >>> 'Electric Counterpoint' in list(songs)
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> d = {'Joe':123, 'Jane':234}
          >>> sorted(list(d.keys()))
          ['Jane', 'Joe']
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'type': 'wwpp'
    }
  ]
}
