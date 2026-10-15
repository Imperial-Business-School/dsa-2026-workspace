test = {
  'name': 'Extending Monster Class',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'answer': '453cf288da1dfd386b98842f7679fc94',
          'choices': [
            '1',
            '3',
            '4',
            '5'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Let's introduce a new class Attack(object):
          
          class Attack(object):
            def __init__(self, name, attack_type, damage):
                self.name = name
                self.attack_type = attack_type
                self.damage = damage
          
            def get_attack_type(self):
                return self.attack_type
          
            def get_damage(self):
                return self.damage
          
            def __str__(self):
                return self.name
          
          
          Q: How many parameters need to be given when instantiating this class?
          """
        }
      ],
      'scored': True,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'answer': 'ea18993f8405572bde4b654a3b876282',
          'choices': [
            "(2 elements) Attacking monster's attack damage points and target monster's health",
            "(4 elements) Attacking monster's and target monster's attack damage and combat points",
            "(3 elements) Attacking monster's attack damage and combat points, and target monster's combat points",
            "(2 elements) Attacking monster's and target monster's attack damage points"
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Let's extend the Monster(object) class by adding the constructor parameters and with two additional methos:
          Assume the class Attack(object) has been defined as above
          class Monster(object):
            def __init__(self, name, monster_type, combat_points, hit_points, attacks):
                self.name = name
                self.monster_type = monster_type
                self.combat_points = combat_points
                self.hit_points = hit_points
                self.health = hit_points
                self.attacks = attacks
          
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
          
            def hurt(self, damage):
                self.health = self.health - damage
                if self.health <= 0:
                    print(self.name + ' is dead!')
                else: print(self.name + ' has ' + str(self.health) + ' health left.')
          
            def heal(self, healing):
                self.health = min(self.hit_points,self.health + healing)
                if self.health == self.hit_points:
                    print(self.name + ' is in full strength!')
                else: print(self.name + ' has ' + str(self.health) + ' health left.')
          
            def use_attack(self, attack, target_monster):
                if attack not in self.attacks:
                    print(self.name + ' does not have this attack!')
                else:
                    damage = attack.get_damage()
                    damage = round(damage * self.combat_points / target_monster.get_combat_points())
                    print(self.name + ' hits ' + str(target_monster) + ' for ' + str(damage) + 'damage!')
                    target_monster.hurt(damage)
          
          
          Q: How many elements does the use_attack method use to determine the damage applied to the target_monster?
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
          >>> # Let's now test one fight example:
          >>> class Monster(object):
          ...      def __init__(self, name, monster_type, combat_points, hit_points, attacks):
          ...          self.name = name
          ...          self.monster_type = monster_type # type
          ...          self.combat_points = combat_points
          ...          self.hit_points = hit_points
          ...          self.health = hit_points # current health
          ...          self.attacks = attacks
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
          ...          else: print(self.name + ' has ' + str(self.health) + ' health left.')
          ...      def heal(self,healing):
          ...          self.health = min(self.hit_points,self.health + healing)
          ...          if self.health == self.hit_points:
          ...              print(self.name + ' is in full strength!')
          ...          else: print(self.name + ' has ' + str(self.health) + ' health left.')
          ...      def use_attack(self,attack,target_monster):
          ...          if attack not in self.attacks:
          ...              print(self.name + ' does not have this attack!')
          ...          else:
          ...              damage = attack.get_damage()
          ...              damage = round(damage * self.combat_points / target_monster.get_combat_points())
          ...              print(self.name + ' hits ' + str(target_monster) + ' for ' + str(damage) + ' damage!')
          ...              target_monster.hurt(damage)
          >>> # We first create 2 attack types:
          >>> lightning = Attack('LightningBolt', 'electric', 20)
          >>> spray = Attack('WaterSpray', 'water', 10)
          >>> # We now create 2 Pokemons:
          >>> pika = Monster('Pikachu', 'electric', 100, 80,[lightning])
          >>> squirt = Monster('Squirtle','water',200,50,[spray])
          >>> # Pikachu attacks Squirtle!
          >>> pika.use_attack(lightning, squirt)
          970721e7593716ed3efced9657c7cf37
          899f23bb350395097d58c097a6b662bf
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'answer': '5c812d04a01c54bd2b0ce183a213419e',
          'choices': [
            '80',
            '70',
            '60',
            '50'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Q: How many health points would pika have remaining after squirt attacked it with:
          squirt.use_attack(spray,pika)
          ?
          """
        }
      ],
      'scored': True,
      'type': 'concept'
    }
  ]
}
