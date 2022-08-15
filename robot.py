from unicodedata import name

from .dinosaur import Dinosaur
from .weapon import Weapon


class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Lazor", 28)
        pass
    
    def attack(self, dinosaur):
        self.dinosaur = dinosaur

    # def __init__(self):
    #     self.player.name = "name"
    #     self.player.health = 100
    #     self.active_weapon = Weapon()

    # def attack(self):
    #     self.active_weapon = Weapon()

    

    # # def attack(self, attack):
    # #     self.dinosour = attack


    # def attack_dino(self, use_weapon):
    #     self.dinosour = use_weapon
        

    # def weapon(self, attack):
    #     self.active_weapon = attack

    # # def attack(self, dinosour):
    # #     self. = dinosour

    # # def weapon(self, attack_power):
    # #     self.active_weapon = attack_power
