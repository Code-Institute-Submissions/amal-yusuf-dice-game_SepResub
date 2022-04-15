import random

class Die:
    """
    Create instance of Die
    """
    def __init__(self, human_player, computer_player):
        self.haman_palyer = human_player
        self.computer_player = computer_player
        self.score = 0
    
    def move(self):
        """
        Switches turn between players
        """
        if self.human_player:
            self.human_move()
        else:
            self.computer_move()
    
    def dice(self):
        """Returns the rolled dice of random int between 1 and 6"""
        self.rollDice = random.randint(1, 6)
        print(f"You rolled a", {self.rollDice})

