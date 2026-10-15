test = {
  'name': 'Monster_use_attack',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> lightning = Attack('LightningBolt', 'electric', 20)
          >>> spray = Attack('WaterSpray', 'water', 10)
          >>> pika = Monster('Pikachu', 'electric', 100, 80, [lightning])
          >>> squirt = Monster('Squirtle', 'water', 200, 50, [spray])
          >>> pika.use_attack(lightning, squirt)
          Pikachu hits Squirtle for 10!
          Squirtle has 40 health left.
          >>> squirt.use_attack(spray, pika)
          Squirtle hits Pikachu for 20!
          Pikachu has 60 health left.
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
