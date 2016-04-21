import time
from MancalaBoard import *
import math
import time

execfile("MancalaGUI.py")

# create mancala pllayers
me1 = MancalaPlayer(1, Player.ABPRUNE)
me2 = MancalaPlayer(1, Player.MINIMAX)
player1 = MancalaPlayer(2, Player.MINIMAX)
player2 = Player(2, Player.RANDOM)
player3 = Player(2, Player.MINIMAX)

#opponents = [player2, player3, player4]
mes = [me1, me2]
opponents = [player3]


myBoard = MancalaBoard()


iterations = 2

for meNume, me in enumerate(mes):

    for oppNum, currentOpponent in enumerate(opponents):

        #reset the scores
        p1 = 0
        p2 = 0
        
        
        print ""
        print "***********************************************"
        print "me" + str(meNume + 1) + " playing against opponent" + str(oppNum + 1)

        elapsed = 0

        for i in enumerate(range(1,iterations)):   
                           
                        
            start_time = time.time()
            winner = myBoard.hostGame(me, currentOpponent)
            elapsed = float(elapsed) + float(time.time() - start_time)
                    
            if winner == '1':
                p1 = p1 + 1
            elif winner == '2':
                 p2 = p2 + 1
            else:
                 continue
                             

        percent_won = float(p1) / float(iterations)
        percent_lost = float(p2) / float(iterations)
        #percent_tied = float(iterations - (p1 + p2)) / float(iterations) * 10


        print "You won: " + str(percent_won) + "%\nOpponent won: " + str(percent_lost) + "%"
        print "Average time to play: " + str(float(elapsed)/float(iterations))
        if p1 >= p2:
            print "YOU WON!"
        else:
            print "YOU LOST..."
            
        
print ""
        
    
    


