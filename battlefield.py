from robot import Robot
from dinosaur import Dinosaur  

class BattleField:

    def __init__(self):
        self.robot = Robot("Donkey")
        self.dinosaur = Dinosaur("Ramboo", 30)

    def run_game(self):
        user_input = input("run game")

    def display_message(self):
        print("welcome to Robot vs Dinosaur!")

    def battle_phase(self):
        self.battle_phase = BattleField()
    
    def display_winner(self):
        print(BattleField.display_winner)
        
        
        
        
        # self.run_game = "start"
        # self.display_welcome = "welcome"
        # self.battle_phase = 1
        # self.display_winner = "dinosaur"




    # def __init__(self):
    #     self.robot = Robot()
    #     self.dinosaur = Dinosaur()

    # def game(self, start, battle_phase, winner):
    #     self.run_game = start
    #     self.display_welcome = "Welcome to the battle dome"
    #     self.battle_phase = battle_phase
    #     self.display_winner = winner
    
    # # while Robot 

    # # def __init__(self):
    # #     self.run_game = 
    # #     self.display_message = "words"
    # #     self.battle_phase = 
    # #     self.display_winner = 


    # # def robot(self):
        