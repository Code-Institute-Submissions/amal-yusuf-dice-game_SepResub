import random


class PlayGame:
    """
    Create instance of playermixin class have methods rolldice and hold
     """
    def __init__(self):
        self.total = 0
        self.score = 0

    def rolldice(self):
        """
        This method generate random number between 1 and 6
        """
        dienb = random.randint(1, 6)
        print("The player got " + str(dienb))  # print result
        print('-' * 40)

        if dienb == 1:  # turn ends if player got 1
            self.score = 0
            return dienb
        else:
            # else, add the die number to the score
            self.score = self.score + dienb
            return dienb

    def hold(self):
        """
        only add the score to the total when the user chooses to hold
        """
        self.total = self.total+self.score
        self.score = 0

    def checkwin(self):
        """
        if 100 needs to be changed, also change in main code (after #STARTGAME)
        """
        while (self.total > 10):
            if self.total > 10:
                return True
            else:
                return False


class Human(PlayGame):
    """
    Create instance of human class which has attributes: name, total,
    turnscore and uses methods from playermixin class
    """
    def __init__(self, name):
        """
        inherits the super attributes, and has additional attribute name
        """
        super().__init__()
        self.name = name

    def doturn(self):
        print("Now it is the turn of " + self.name)
        print('-' * 40)

        while True:
            # this while loop to repeat only if the user didn't
            # give a valid input for roll or hold
            move = input("Would you like to roll(r) die or hold(h)?")
            print('-' * 40)

            if move == 'h':
                super().hold()
                break
            elif move == 'r':
                dienb = super().rolldice()
                if dienb == 1:
                    # round_score=0
                    # move='h'
                    break
            else:
                print("please input valid answer.")
                print('-' * 40)


class CPU(PlayGame):
    """
    Create instance of a cpu class which has attributes score, total,
    and uses methods from playermixin class
    """
    def __init__(self):
        super().__init__()

    def doturn(self):
        print("Now it is the CPU's turn.")
        print('-' * 40)

        while True:
            move = random.randint(1, 4)
            if move == 4:  # hold
                print("CPU player will hold.")
                print('-' * 40)

                super().hold()
                print()
                break
            elif move < 4:  # rolldie
                dienb = super().rolldice()
                if dienb == 1:
                    break

# STARTGAME

print()
print('-' * 40)
print('-' * 40)
print()
print('Welcome to the Dice Pig Game!')
print()
print('-' * 40)
print('-' * 40)

# ask user if he wants to play against CPU or users

game = input("Would you like to play against the CPU(c) or a human(h)? (c/h)")
print('-' * 40)

if game == 'c':  # user chooses cpu
    name1 = input("Please insert your name:")
    print('-' * 40)
    # both players initialised
    player1 = Human(name1)
    cpu1 = CPU()

    while True:
        player1.doturn()
        if player1.checkwin():   # checks if player1 has won, end game
            print(player1.name + "  has won! Congrats!.")
            print('-' * 40)

            break   # exit the while loop
        cpu1.doturn()
        if cpu1.checkwin():
            print(player1.name + "  has lost.")
            print('-' * 40)

            break
elif game == 'h':
    while True:
        try:
            nbplayers = int(input("How many players would you like?"))
            print('-' * 40)
            # initialising list of players
            players = {}
            for i in range(nbplayers):
                name = input("Please insert name of player " + str(i + 1) + ":")
                # initialise a human player
                # and place him/her in the players list
                players[i] = Human(name)
                print('-' * 40)
            while True:
                for i in range(nbplayers):
                    #  give each each player a turn
                    players[i].doturn()
                    if players[i].checkwin():
                        print(players[i].name + " has won.")
                        print('-' * 40)
                        break
                if players[i].checkwin():
                    break
            break
        except:
            print("Please input a number next time. Try again now.")
else:
    print("You inputted an invalid input.")
    print('-' * 40)
