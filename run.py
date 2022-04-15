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
        # print(f"You rolled a", {self.rollDice})

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

    def computer_move(self):
        """Creates a while loop for the computer's turn"""
        round_score = 0
        rollagain = 'y'
        while rollagain == 'y':
            roll = self.rollDice 
            if roll == 1:
                print("Computer rolled a 1", roll)
                round_score = 0
                rollagain = 'n'
            else:
                print(f"Computer rolled a ", {self.rollDice})
                round_score = round_score + self.rollDice
                if round_score < 20:
                    print("Computer will roll again")
                else:
                    rollagain = 'n'
        self.score += round_score
        print("Cumputer's turn is over")
        print("Computer's round score is ", round_score)
        print(f"Computer's total score is  \n", {self.score})

    # def play_game(self):
    #     """
    #     This function will manage the game and is not created yet
    #     """


#  The start_game variable is not defined yet 
# start_game = Die("human_player", "computer_player")
# start_game.play_game()
# print(start_game.play_game())

    def StartGame():
        ''' Displays a welcome message for the game and start the game'''
        human_score = 0
        computer_score = 0
        human_score < 100 and computer_score < 100:
        print("-" * 35)
        print("        ***     ")
        print("Welcome to Dice Pig Game!")
        print("        ***     ")
        print("The current score is ")
        print("Human_Player is : ", human_score)
        print()
        print("Computer is : ", computer_score)
        print("-" * 35)
        human_player = input("Please enter your name: \n")
        print("-" * 35)
        start_game = Die("human_player", "compuer_player")

StartGame()






