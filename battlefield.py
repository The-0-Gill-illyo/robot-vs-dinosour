from robot import Robot
from dinosaur import Dinosaur  

class BattleField:

    def __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()

    def game(self, start, battle_phase, winner):
        self.run_game = start
        self.display_welcome = "Welcome to the battle dome"
        self.battle_phase = battle_phase
        self.display_winner = winner
    

    # def __init__(self):
    #     self.run_game = 
    #     self.display_message = "words"
    #     self.battle_phase = 
    #     self.display_winner = 


    # def robot(self):
        