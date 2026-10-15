test = {
  'name': 'Building Monster Class',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'answer': '5',
          'choices': [
            '1',
            '3',
            '5',
            '10'
          ],
          'hidden': False,
          'locked': False,
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
          'answer': '7',
          'choices': [
            '1',
            '3',
            '5',
            '7',
            '10'
          ],
          'hidden': False,
          'locked': False,
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
          'answer': 'str(pika)',
          'choices': [
            'pika.name',
            'pika.print()',
            'str(pika)',
            'del pika'
          ],
          'hidden': False,
          'locked': False,
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
          Pikachu has 70 health left!
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
