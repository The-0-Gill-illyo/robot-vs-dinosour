from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon
from battlefield import BattleField

raptor = Dinosaur("Godzilla", 28)

transformer = Robot("Bumble-bee")

battle_axe = Weapon("battle-axe", 35)

desert = BattleField()

# transformer.active_weapon.Robot(Weapon(battle_axe, 35))

raptor.attack(transformer.active_weapon(Weapon(battle_axe, 40))).desert -= transformer.attack(raptor.attack_power).desert 

# Robot.attack(Dinosaur(Weapon("Battle-axe", 35))).transformer -= Dinosaur("Godzilla", 28).raptor

# print(Robot.attack(Robot(transformer), Dinosaur(raptor, 28)))

# print(BattleField.display_winner)