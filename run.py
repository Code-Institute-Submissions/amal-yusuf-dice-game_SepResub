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

    def human_move(self):
        """Creates a while loop for the human's turn"""
        round_score = 0
        rollagain = 'y'
        while rollagain  == 'y':
            roll = self.rollDice  
            if roll == 1:
                print('You rolled a 1', roll)
                round_score = 0
                rollagain = 'n'
            else:
                print(f"You rolled a ", {self.rollDice})
                round_score = round_score + self.rollDice
                print("Your's round score is ", round_score)
                rollagain = input('Would like to roll again? (y/n)')
        self.score += round_score
        print("Your turn is over")
        print(" your total score is  \n", {self.score})


