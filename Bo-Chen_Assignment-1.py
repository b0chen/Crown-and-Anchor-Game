"""
Bo Chen (10190141)
CISC 121 Assigment 1: Crown and Anchor
June 10, 2017

This is a Python version 3.6 of the Crown and Anchor Game.
Each player puts a wager on one or more of the symbols on the wheel. 
The wheel is then spun, and players recieve points if their wager was on the spin.
Detailed rules can be found here: https://goo.gl/evbMrE
"""
import random

"""
The round() function runs all the functions required for each round.
It takes the playersScore and loops until all players have 0 points.
"""
def round(playerScore):
    #checks if game is over
    endGameCheck(playerScore)
    #asks for bets
    for key in playerScore:
        if playerScore[key][0] !=0:
            for i in range (0,6):
                #collects wagers
                bet(playerScore[key],i,key)
    #calculates winnings
    winnings(playerScore)    
    #clears previous round's bets
    clearBets(playerScore)
    #loops round function
    round(playerScore)

"""
The clearBets() function clears all the bets from the previous round
It takes the playerScore and sets all the bets to 0
"""
def clearBets(playerScore):
    for key in playerScore:
        for i in range (1,7):
            playerScore[key][i] = 0

"""
The winnings() function calcualtes all the winnings of the round
making sure to keep track of the number of Anchor winnings.
It takes playerScore and determins which player won how much.
"""
def winnings(playerScore):
    spin = spinWheel()
    print ("\n\nThe spin is:", spin)
    symbols = ["hearts", "spades", "dimonds", "clovers", "crowns", "anchors"]
    for key in playerScore:
        #keeps track of their winnings this round
        totalWinnings = 0
        anchorFlag = 0
        winFlag= [0,0,0,0,0,0]
        for s in spin:
            for x in range(1,7): 
                # if the symbol spun matches the player's wager
                if s == symbols[(x-1)] and playerScore[key][x] > 0:
                    playerScore[key][0] = playerScore[key][0] +  playerScore[key][x]
                    totalWinnings = totalWinnings +  playerScore[key][x]
                    # checks if the player already recieved their points back for this symbol
                    if winFlag[x-1] == 0:
                        winFlag[x-1] = 1
                        playerScore[key][0] = playerScore[key][0] + playerScore[key][x]
                        totalWinnings =  totalWinnings + playerScore[key][x]
            #checks if the player wagered anchors and if three anchors were spun
            if s == "anchors" and playerScore[key][6] > 0:
                anchorFlag = anchorFlag + 1
            if anchorFlag == 3:
                print("CISC 121 -  Winner on Anchors!!!!")
        print ("Player ", key,"'s", "winnings is:", totalWinnings)
    #displays players coins after winning
    for name in playerScore:
        print("Player ",name," has ",playerScore[name][0]," coins")
    return(playerScore,spin)

"""
The spinWheel() function randmly chooses one of the possible spins from
the Crown and Anchor wheel.
"""
def spinWheel():
    wheel = [["spades","spades","spades"],["clovers","dimonds","dimonds"],
    ["crowns","crowns","crowns"],["clovers","crowns","hearts"],["spades","spades","hearts"],
    ["spades","dimonds","crowns"],["anchors","anchors","anchors"],["clovers","clovers","dimonds"],
    ["hearts","hearts","hearts"],["anchors","crowns","crowns"],["clovers","clovers","clovers"],
    ["spades","hearts","hearts"],["dimonds","dimonds","dimonds"],["crowns","anchors","anchors"]]
    return(random.choice(wheel))

"""
The bet() function accepts user's imput (bets) making sure the bets are 
allowed (0, 1, 2, 5, 10), and that the player has sufficient funds. 
It takes playerScore, a option position, and the current player betting
it updates the bets into playerScore.
"""
def bet(playerScore,i,player):
    validBets = [0,1,2,5,10]
    options = ['hearts', 'spades', 'diamonds', 'clubs', 'crowns', 'anchors']
    numCoins = 0
    #displays current bets
    print("\nPlayer:",player,"current bet \n hearts:    ",playerScore[1],"\n spades:    ",
        playerScore[2],"\n diamonds:  ",playerScore[3],"\n clubs:     ",playerScore[4],
        "\n crowns:    ",playerScore[5],"\n anchors:   ",playerScore[6])
    print("Player:",player,"you have ",playerScore[0]," coin remaining")    
    #records valid bets
    try:
        print("How many coins (0, 1, 2, 5, 10) would you like to bet on",options[i],"? ")
        numCoins = int(input())
    except:
        print("\n\n--- Please enter a valid bet ---")
        bet(playerScore,i,player)
    #checks if the bet is a valid option
    if numCoins in validBets:
        #checks if player has sufficient funds
        if ((playerScore[0] - numCoins) >= 0):
            playerScore[0] = playerScore[0] - numCoins
            playerScore[i+1] = numCoins
        else:
            print("\n\n--- You don't have enough coins ---")
            bet(playerScore,i,player)
    else:
        print("\n\n--- Please enter a valid bet ---")
        bet(playerScore,i,player)
    return playerScore

"""
The endGameCheck() functuin check to see if all player have 0 points
if so, the game ends. It takes the playerScore and check the amout of coins
"""
def endGameCheck(playerScore):
    flag = True 
    for key in playerScore:
        if playerScore[key][0] != 0:
            flag = False 
    if flag == True:
        print ("Thank you for playing")
        quit()
    else:
        return   

"""
The main() function intiates the game for the number of players.
It accepts user input to determin the number of players.
"""
def main():
    playerScore = {}
    print("Welcome to the Crown and Anchor Game! \n")
    try:
        numPlayers = int(input("How many players will there be? \n"))
    except:
        print('\n' * 50)
        print("---Please enter a valid digit \n---")
        main()
    for i in range (1,numPlayers+1):
        # playerScore is a dictionary containioneach player's information
        # player# 's [coins, hearts, spades, diamonds, clubs, crowns, anchors]
        playerScore[i] = [10,0,0,0,0,0,0]
    for name in playerScore:
        print("Player ",name," has ",playerScore[name][0]," coins")
    round(playerScore)
    
main()