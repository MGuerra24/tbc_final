import random

class Character(object):
    def __init__(self, name = "Damian",
                 hitPoints = 15,
                 hitChance = 45,
                 maxDamage = 6,
                 armor = 1):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        self.__hitPoints = value
    
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        self.__hitChance = value
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        self.__maxDamage = value
    
    @property
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, value):
        self.__armor = value

    def printStats(self):
        print(f"""
        Name : {self.name}
        Health : {self.hitPoints}
        Hit Chance : {self.hitChance}
        Max Damage : {self.maxDamage}
        Armor : {self.armor}
        """)
        
    def hit(self, enemy):
        if random.randint(1, 100) < self.hitChance:
            print (f"{self.name} hits {enemy.name}...")
            damage = random.randint(1, self.maxDamage)
            print (f" for {damage} points of damage...")
            damage -= enemy.armor
            if damage < 0:
                damage = 0
            if enemy.armor > 0:
                print(f" but {enemy.name}'s armor absorbed {enemy.armor} points")
            enemy.hitPoints -= damage
        else:
            print(f"{self.name} misses {enemy.name}")
            
    def testInt(self, value, min = 0, max = 100, default = 0):
        out = default

        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")

        return out
        
    def fight(self, hero, enemy):
        keepGoing = True
        while keepGoing:
            hero.hit(enemy)
            enemy.hit(hero)
            
            print(f"{hero.name} HP : {hero.hitPoints}")
            print(f"{enemy.name} HP : {enemy.hitPoints}")
            print()
            
            if hero.hitPoints <= 0:
                print(f"{hero.name} loses")
                keepGoing = False
            elif enemy.hitPoints <= 0:
                print(f"{enemy.name} loses")
                keepGoing = False
                
            dummy = input("Press <ENTER> for another round")