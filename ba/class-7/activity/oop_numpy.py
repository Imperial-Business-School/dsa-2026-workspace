
class Monster(object):
    """
    Monsters
    
    Attributes:
        name: string
        monster_type: string
        combat_points: nonnegative number - strength in combat
        hit_points: nonnegative number - maximum health level
        health: nonnegative number - current health level
        attacks: list of the monster's attacks (items are Attack objects)
                
    """
    def __init__(self, name, monster_type, combat_points, hit_points, attacks=None):
        """
        Initialize a new Monster
        
        You do NOT need to edit this function or its arguments.
        If you do, you might break something!
        
        Notice that attacks is an optional argument.
        """
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
        """
        Returns string representation of the Monster. Here just the name.
        """
        return self.name

    def hurt(self, damage):
        """
        Hurt monster. Reduce its health by damage down to a minimum of zero.
        
        Parameters:
            damage: number
            
        """
        self.health = max(self.health - damage, 0)
        if self.health <= 0:
            print(self.name + ' is dead!')
        else: print(self.name + ' has ' + str(self.health) + ' health left.')
    
    def heal(self, healing_points):
        """
        Heal the monster. 
        
        Parameters:
            healing_points: number
        
        Increase the monster's health by "healing_points" up to a maximum of hit_points
        Print out the health status as specified in the examples below.
        
        Assume health is positive after healing.
        
        Examples:
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
        """
        # DON'T CHANGE ANYTHING ABOVE
        # YOUR CODE BELOW
        self.health = min(self.hit_points, self.health+healing_points)
        if self.health == self.hit_points:
            print("{} is in full strength!".format(self.name))
        else:
            print(f"{self.name} has {self.health} health left.")
            
    def use_attack(self, attack, target_monster):
        """
        Use Attack on target monster
        
        attack is an Attack - implement this class below first.
        
        Checks if attack is one of this Monster's attacks.
        If not, print out a message stating the Monster does not have this attack
        If it is, calculate damage from the attack as DAMAGE, where
            DAMAGE = (attack damage)*(this monster's combat points)/(target monster's combat points)
            DAMAGE should be rounded to an integer value
            
            then print out that the attack is taking place as in the examples below
            
            then hurt the target monster by DAMAGE    
        
        Examples:
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
        """
        if attack not in self.attacks:
            print(self.name + ' does not have this attack!')
        else:
            damage = round(attack.get_damage() * self.combat_points/target_monster.get_combat_points())     
            print(f"{self.name} hits {target_monster.name} for {damage}!")
            target_monster.hurt(damage)

# Create the Attack class as described in the instructions:
class Attack(object):
    """
    Attack class for Monsters
    """
    def __init__(self, name, attack_type, damage):
        """
        Initialise Attack
        """
        self.name = name
        self.attack_type = attack_type
        self.damage = damage
        
    
    def get_attack_type(self):
        """
        Return attack type
        """
        return self.attack_type

    def get_damage(self):
        """
        Return attack damage
        """
        return self.damage
    
    def __str__(self):
        return self.name


def test_attack():
    """
    OK tests for the Attack() class.
    
    Examples:    
    >>> lightning = Attack('LightningBolt', 'electric', 20)    
    >>> lightning.get_attack_type()
    'electric'
    >>> lightning.get_damage()
    20
    """
    # DON'T EDIT THIS FUNCTION
    pass
   

