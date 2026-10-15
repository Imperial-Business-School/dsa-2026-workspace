test = {
  'name': 'Big O Extra',
  'points': 14,
  'suites': [
    {
      'cases': [
        {
          'answer': '636655b948fbfa533a325b8ac792c83e',
          'choices': [
            'O(n)',
            'O(n!)',
            'O(n**2)',
            'O(log(n)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the big-O complexity in terms of the size of the input (e.g. assuming a list L of length n)?:
          
          >>> u = 0
          >>> for item in L:
          >>>     u = u + item**2
          >>>     u = u - item
          """
        },
        {
          'answer': 'e7dd09f2d46bcf5233a5d79ca6d6a55d',
          'choices': [
            'O(n)',
            'O(log(n)',
            'O(n**2)',
            'O(n!)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the big-O complexity in terms of the size of the input (e.g. assuming a list L of length n)?:
          
          >>> s = 0
          >>> for index in range(len(L)):
          >>>     L[index] = L[index] + 1
          >>>     for item in L:
          >>>         s = s + item
          """
        },
        {
          'answer': 'e7dd09f2d46bcf5233a5d79ca6d6a55d',
          'choices': [
            'O(n**2)',
            'O(n)',
            'O(log(n)',
            'O(n!)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the big-O complexity in terms of the size of the input (e.g. assuming n is a non-negative integer)?:
          
          >>> y = 0
          >>> i = n
          >>> while i > 0:
          >>>     j = i
          >>>     while j > 0:
          >>>         y += 1
          >>>         j -= 1
          >>>     i -= 1
          """
        },
        {
          'answer': 'aa8983acb308de07a785373d3973fd8a',
          'choices': [
            'A, D, C, B',
            'D, A, B, C',
            'A, B, C, D',
            'B, A, D, C',
            'None of the others'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How would you rate the following functions in increasing order of big-O complexity?
          		  A: n*log(n) 
          		  B: n**2
          		  C: 2**n
          		  D: n*log(2)
          """
        }
      ],
      'scored': True,
      'type': 'concept'
    }
  ]
}
