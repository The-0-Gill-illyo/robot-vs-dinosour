class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        self.robot = robot
        

    # def __init__(self):
    #     self.name = "name"
    #     self.health = 100
    #     self.attack_power = 16

    # def attack(self, robot):
    #     self.attack_power = robot

    # # def robot_attack(self, name, attack):
    # #     self.robot = attack
    # #     pass    

    # # # def robot_attack(self, attack):
    # # #     self.attack_power = attack


    # # # # def robo_attack(self, attack):
    # # # #     self.robot = attack