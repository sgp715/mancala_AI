import time
from MancalaBoard import *
import math
import time
import difflib
import sys
import StringIO
import difflib

# load the files
execfile("MancalaGUI.py")

# should we write a report
report = raw_input("Should we write a report? [y/n]")
if report == 'y':
    report = True
else:
    report = False
    
logs = raw_input("Should we create logs? [y/n]")
if logs == 'y':
    logs = True
else:
    logs = False


# create mancala pllayers
# only compare two players
me1 = MancalaPlayer(1, Player.ABPRUNE,3)
me2 = MancalaPlayer(1, Player.MINIMAX,3)
player1 = MancalaPlayer(2, Player.MINIMAX)
player2 = Player(2, Player.RANDOM)
player3 = Player(2, Player.MINIMAX)

#opponents = [player2, player3, player4]
mes = [me1, me2]
if logs:
    assert len(mes) == 2
    
opponents = [player1]


myBoard = MancalaBoard()

iterations = 100

filesDict = {}

for meNum, me in enumerate(mes):
        
    if report: print "***********************************************"
        
    if logs: sys.stdout = filesDict[meNum] = StringIO.StringIO()
        
    for oppNum, currentOpponent in enumerate(opponents):

        #reset the scores
        p1 = 0
        p2 = 0
            
            
        if report: print "me" + str(meNume + 1) + " playing against opponent" + str(oppNum + 1)

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

            
        if report:
            print "You won: " + str(percent_won) + "%\nOpponent won: " + str(percent_lost) + "%\n"
            print "Average time to play: " + str(float(elapsed)/float(iterations))+ "\n"
            
            

# reset stdout
sys.stdout = sys.__stdout__

#filesDict[string].getvalue()
if logs:
    diff = difflib.ndiff(filesDict[0].getvalue(), filesDict[1].getvalue())
    print "***********************************************"
    print "                 DIFFERENCES                   "
    print ''.join(diff),
