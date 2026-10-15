test = {
  'name': 'test_queue',
  'points': 11,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> Q = Queue()
          >>> Q.enqueue(2)
          >>> Q.enqueue(1)
          >>> str(Q)
          '2 1 '
          >>> x = Q.dequeue()
          >>> str(Q)
          '1 '
          >>> Q = Queue()
          >>> A = [135, 891, 886, 537, 253, 6, 635, 577, 331, 192]
          >>> if Q.is_empty():
          ... 	for i in A:
          ... 		Q.enqueue(i)
          >>> for i in range(int(len(Q)/2)):
          ...     z = Q.dequeue()
          >>> str(Q)
          '6 635 577 331 192 '
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
