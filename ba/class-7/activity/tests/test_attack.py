test = {
  'name': 'test_attack',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> lightning = Attack('LightningBolt', 'electric', 20)
          >>> lightning.get_attack_type()
          'electric'
          >>> lightning.get_damage()
          20
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
