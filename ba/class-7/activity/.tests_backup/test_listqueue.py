test = {
  'name': 'test_listqueue',
  'points': 11,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> LQ = ListQueue()
          >>> LQ.enqueue(2)
          >>> LQ.enqueue(1)
          >>> print(LQ.items)
          [2, 1]
          >>> x = LQ.dequeue()
          >>> print(LQ.items)
          [1]
          >>> LQ = ListQueue()
          >>> A = [135, 891, 886, 537, 253, 6, 635, 577, 331, 192]
          >>> if LQ.is_empty():
          ...     for i in A:
          ...         LQ.enqueue(i)
          >>> for i in range(int(len(LQ.items)/2)):
          ...     z = LQ.dequeue()
          >>> print(LQ.items)
          [6, 635, 577, 331, 192]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from oop_numpy_extra import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
