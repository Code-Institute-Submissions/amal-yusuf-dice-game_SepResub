# Dice Game Pig:

Dice Game is a python terminal game, which runs in the code institute mock terminal on Heroku.
The rules of this game:

## How to play

You will need a one dice to play.
The game is a very simple dice game in which two players or more race to reach 100 points. Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player holds and scores the sum of the rolls (i.e. the turn total). You can eaither paly against the CPU or other users, one or multiple users. At any time during a player's turn, the player is faced with two decisions:

•	move  == “r” - If the player rolls a:

o	1: the player scores nothing and it becomes the opponent's turn.

o	2 - 6: the number is added to the player's turn total and the player's turn continues.

•	move == “h” - The turn total is added to the player's score and it becomes the opponent's turn.

You are playing against the computer or other users, two or more players can join the game.

You can read more about it on Wikipedia  (https://en.wikipedia.org/wiki/Pig_(dice_game))

#### Here is the live version of my completed project:https://dice-playing.herokuapp.com/
![image](https://user-images.githubusercontent.com/91415085/190574118-c3de973f-e10d-449a-8ff3-dcccce459131.png)


## Features 
### Exixting Features:
- Welcome page to the game, on this page, you will be asked wether you would like to play against the CPU or Human.
![image](https://user-images.githubusercontent.com/91415085/190576672-aa5179cb-37b6-4931-bee0-07d3df6266e8.png)
- If you choose to play against CPU or Human, you will be asked to input your name 
![image](https://user-images.githubusercontent.com/91415085/190576967-4dd676bf-af52-458f-bdfc-e4cb259e5fdb.png)
- Also you can choose to play with multiple players as shown below, by inputting the number of players and then insert their names. 
- Each player will play their turn untill he/she decide to hold or roll a 1, then the turn will switch to the next player.
- If the player rolls a 1, their score will round up to zero, and will start again from zero on the next turn
![image](https://user-images.githubusercontent.com/91415085/190580793-6597cbe4-8f40-46bc-b268-0237032f472e.png)
- Input validation and error checking
• At the moment the application is checking the validation when rolling or holding the dice 
• I will add more validation to the code to make it more interactable for the user, and to make it more fun when playing the game
![image](https://user-images.githubusercontent.com/91415085/190583804-d588a85c-169f-4eb8-b8c2-840a329807ee.png)


### Future features to be added;
- To show the round score and the total score of the player who is playing 
- To show the final score of all players when the game is finished
- To show the total score of the player, when he/she, or the cpu rolls a 1
- Add extra validation to the code

## Testing 

### Bugs
No bugs 

### Remaining bugs
No bugs remaining 


### Validator Testing

I have tested the code manually through PEP8 linear and confirmed no errors.
![image](https://user-images.githubusercontent.com/91415085/190574466-047bb87b-0962-4cd4-a32f-8b9bb3fd3f2e.png)


## Deployment

This project was deployed using Code Institute's mock terminal for Heroku

 ### •Steps for deployment:
 
 - Fork or clone this repository
 - Create a new Heroku app
 - Set the build backs to Python or NodeJS in that order
 - Link the Heroku app to the repository 
 - Click on deploy

 
## Credits

- Code Institute for the deployment terminal 
- Lecture 11 on Object Oriented Programming in Python (Dice Pig Game) : http://www.cs.columbia.edu/~cannon/1006/lecture11.html
 

