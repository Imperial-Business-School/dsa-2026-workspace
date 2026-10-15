test = {
  'name': 'Big O ',
  'points': 14,
  'suites': [
    {
      'cases': [
        {
          'answer': 'cbc9f464f9b6cbdc109d587964eb470f',
          'choices': [
            'n times',
            '2n times',
            'n**2 times',
            'log(n) times'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How many times will Python print 'Hello!'?:
          (n is a positive integer number)
          
          >>> for i in range(n):
          >>>     print('Hello!')
          """
        },
        {
          'answer': '04a1c639522d71ce6baa58175b5adc1b',
          'choices': [
            'n times',
            '2n times',
            'n**2 times',
            'log(n) times'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How many times will Python print 'Hello!'?:
          (n is a positive integer number)
          
          >>> for i in range(n):
          >>>     for j in range(n):
          >>>         print('Hello!')
          """
        },
        {
          'answer': 'ca491d7869cf35180f6740e9e34144b1',
          'choices': [
            'n times',
            '2n times',
            'n**2 times',
            'log(n) times'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How many times will Python print 'Hello!'?:
          (n is a positive integer number)
          
          >>> for i in range(n):
          >>>     print('Hello!')
          >>>     print('Hello!')
          """
        },
        {
          'answer': 'b08739e9405a1bb8b6ee9b8f53a2e906',
          'choices': [
            'n times',
            '2n times',
            'n**2 times',
            'log(n) times'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How many times will Python print 'Hello!'?:
          (n is a positive integer number)
          
          >>> while n > 1:
          >>>     n = int(n/2)
          >>>     print('Hello!')
          """
        }
      ],
      'scored': True,
      'type': 'concept'
    }
  ]
}
