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
