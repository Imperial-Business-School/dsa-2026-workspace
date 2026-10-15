test = {
  'name': 'Monster_heal',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pika = Monster('Pikachu', 'electric', 100, 80)
          >>> pika.heal(20)
          Pikachu is in full strength!
          >>> pika.get_health()
          80
          >>> pika = Monster('Pikachu', 'electric', 100, 50)
          >>> pika.hurt(10)
          Pikachu has 40 health left.
          >>> pika.heal(5)
          Pikachu has 45 health left.
          >>> pika.get_health()
          45
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from oop_numpy import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
