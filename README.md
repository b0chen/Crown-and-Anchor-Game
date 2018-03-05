Bo Chen (10190141)
CISC 121 Assigment 1: Crown and Anchor
June 10, 2017

This is a Python version 3.6 of the Crown and Anchor Game.
Each player puts a wager on one or more of the symbols on the wheel. 
The wheel is then spun, and players recieve points if their wager was on the spin.

Assignment:
"The goal of this assignment is to give you some practice using the Python programming language and structuring programs.  You program must be well structured which means split into appropriate functions, appropriate variable names used and well documented.    

You will write a game to simulate a simple game of "Crown and Anchor" which is a gambling game.  The crown and anchor wheel (which spins around) is shown above. The symbols on the Crown and Anchor "wheel" consist of hearts, spades, diamonds, clubs, crowns and anchors, 3 symbols per "slot" on the wheel. 

Each round, players bet on one or more of the symbols.  The wheel is spun and it stops at one of the slots.  (In the picture above, it has stopped at the slot with 3 anchors.  Let's say the user puts a coin on "hearts".

If there are no hearts in the winning slot they lose their coin
If there is one heart in the winning slot they get their coin back and another coin
If there are 2 hearts in the winning slot they get their coin back and another 2 coins
If there are 3 hearts in the winning slot they get their coin back and another 3 coins
For example, let's say someone bets 2 coins (ie. $2) on hearts -- this is the return:

If there are no hearts in the winning slot they lose the $2.
If there is one heart in the winning slot they get their coins back and another $2 (ie. 2 additional coins)
If there are 2 hearts in the winning slot they get their coins back and another $4 (ie. 4 additional coins)
If there are 3 hearts in the winning slot they get their coins back and another $6 (ie. 6 additional coins)

They may bet in $1, $2, $5 or $10 increments and may place more than one bet per round.    That is, they may place a $2 bet on hearts and a $5 bet on anchors or they may place two $2 bets on hearts.

Each player begins with $10.  You should ask the user how many players there will be in your game when your game begins. When they lose all their money, they are out of the game (that is, they do not place any more bets).   A player may skip any round they wish (ie. not place a bet on a particular round).   If someone wins on 3 anchors, print the phrase "CISC 121 -  Winner on Anchors!!!!".

The game continues while at least one player has money left. 

This game is a text-only game.  To simulate the spinning wheel, you will generate the 3 symbols representing the winning slot at random.  (You may need to read about random number generation in Python).   You will need to represent the players, their current amount of money and the bets using a suitable data structure.  Each round of the game should be as follows:

a) ask for bets -- symbol and amount bet (or skip this round)

b) show the winning "slot"

c) indicate how much was won by each player

d) indicate how much money each player currently has

Repeat the above steps while at least one player has money left.

All of your code MUST be encapsulated within functions. A "main" function will start the program execution. 

Your program must be well documented. Marks are allocated for documentation, neatly organized code, suitable variable names etc. Please refer to the style guide to see what we expect for proper documentation."
