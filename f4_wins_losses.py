# Ryan Bartholomew
# Function 4
# Play the game receiving both team names. Generate random scores without ties. Return W or L.

# Import random
import random

# Receive `HomeTeam` and `VisitingTeam` in that order 
def winLoseSim(home_team, away_team):
    # Make the initial variables
    iHomeScore = random.randint(1,2)
    iVisitorScore = random.randint(1,2)

    # Make the game so it isn't a tie
    bRandKillCode = True
    while bRandKillCode == True:
        if iHomeScore == iVisitorScore:
            iHomeScore = random.randint(1,2)
            iVisitorScore = random.randint(1,2)
        else:
            bRandKillCode = False

    # Return a W or an L
    if iHomeScore > iVisitorScore:
        return "W", iHomeScore, iVisitorScore
    else:
        return "L", iHomeScore, iVisitorScore



'''
PLEASE READ below I have made 2 ways to display the information. One as a string and one as a list please feel
free to use whichever works better

    # As a list
    lFinalList = []
    lFinalList.append = [sHomeTeam, iHomeScore, sOutcome]
    lFinalList.append = [sVisitingTeam, iVisitorScore, sOutcomeVisit]
    return lFinalList

    # As a string
    return (f"{sHomeTeam} score: {iHomeScore}\n{sVisitingTeam} score: {iVisitorScore}\nOutcome: {sOutcome}")

    As a plain W or L
    return sOutcome

game = winLoseSim("BYU", "UVU")
print(game)
'''