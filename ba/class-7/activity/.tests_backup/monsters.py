test = {
  'name': 'Building Monster Class',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'answer': '17676197347896dd77ecff7024cf78ad',
          'choices': [
            '1',
            '3',
            '5',
            '10'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Let's define a Monster class:
          
          class Monster(object):
            def __init__(self, name, monster_type, combat_points, hit_points):
                self.name = name
                self.monster_type = monster_type # type
                self.combat_points = combat_points
                self.hit_points = hit_points
                self.health = hit_points # current health
          
          
          Q: How many attributes does the class have?
          """
        }
      ],
      'scored': True,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'answer': 'c63a6dc2e22cf6f8885c38f5eba00ee3',
          'choices': [
            '1',
            '3',
            '5',
            '7',
            '10'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Let's add some more functionalities:
          
          class Monster(object):
            def __init__(self, name, monster_type, combat_points, hit_points):
                self.name = name
                self.monster_type = monster_type # type
                self.combat_points = combat_points
                self.hit_points = hit_points
                self.health = hit_points # current health
          
            def get_monster_type(self):
                return self.monster_type
          
            def get_combat_points(self):
                return self.combat_points
          
            def get_health(self):
                return self.health
          
            def get_hit_points(self):
                return self.hit_points        
          
            def __str__(self):
                return self.name
          
            def hurt(self,damage):
                self.health = self.health - damage
                if self.health <= 0:
                    print(self.name + ' is dead!')
                else: print(self.name + ' has ' + str(self.health) + ' health left')
          
          
          Q: How many methods does the class Monster() have?
          """
        }
      ],
      'scored': True,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'answer': '9f0aa36f71109789d58873ac820103f2',
          'choices': [
            'pika.name',
            'pika.print()',
            'str(pika)',
            'del pika'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Q:
          Let's assume we have an instance of the Monster() class:
          
          pika = Monster('Pikachu', 'electric', 100, 80) 
          
          Which of the following commands would lead to calling the method:
          
          def __str__(self):
              return self.name
          
          ?
          """
        }
      ],
      'scored': True,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Let's now test some basic functionalities:
          >>> class Monster(object):
          ...      def __init__(self,name,monster_type,combat_points,hit_points):
          ...          self.name = name
          ...          self.monster_type = monster_type # type
          ...          self.combat_points = combat_points
          ...          self.hit_points = hit_points
          ...          self.health = hit_points # current health
          ...      def get_monster_type(self):
          ...          return self.monster_type
          ...      def get_combat_points(self):
          ...          return self.combat_points
          ...      def get_health(self):
          ...          return self.health
          ...      def get_hit_points(self):
          ...          return self.hit_points 
          ...      def __str__(self):
          ...          return self.name
          ...      def hurt(self,damage):
          ...          self.health = self.health - damage
          ...          if self.health <= 0:
          ...              print(self.name + ' is dead!')
          ...          else: print(self.name + ' has ' + str(self.health) + ' health left!')
          >>> pika = Monster('Pikachu', 'electric', 100, 80)
          >>> pika.hurt(10)
          9e9f54b600833bff7adceaa716e0a81f
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
