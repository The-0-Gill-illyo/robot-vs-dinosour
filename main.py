from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon
from battlefield import BattleField

raptor = Dinosaur("Godzilla", 28)

transformer = Robot("Bumble-bee")

battle_axe = Weapon("battle-axe", 35)

desert = BattleField()

Robot.attack(Dinosaur(Weapon("Battle-axe", 40))).transformer -= Dinosaur("Godzilla", 25).raptor

# print(Robot.attack(Robot(transformer), Dinosaur(raptor, 28)))

# print(BattleField.display_winner)