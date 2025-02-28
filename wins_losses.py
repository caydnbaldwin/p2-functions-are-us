# Ryan Bartholomew
# Function 4: Run game with random scores and return a W or L (no ties)
# Play the game receiving both team names. Generate random scores without ties. Return W or L.

#Import Objects
import random

#Make the initial variables
def winLoseSim(sHomeTeam, sVisitingTeam):
    iHomeScore = random.randint(1,2)
    iVisitorScore = random.randint(1,2)

#Make the game so it isn't a tie
    bRandKillCode = True
    while bRandKillCode == True:
        if iHomeScore == iVisitorScore:
            iHomeScore = random.randint(1,2)
            iVisitorScore = random.randint(1,2)
        else:
            bRandKillCode = False

#Return a W or an L
    if iHomeScore > iVisitorScore:
        sOutcome = "W"
    elif iHomeScore < iVisitorScore:
        sOutcome = "L"
    else:
        sOutcome = "Error"
    
    if sOutcome == "W":
        sOutcomeVisit = "L"
    else:
        sOutcomeVisit = "W"

#PLEASE READ below I have made 2 ways to display the information. One as a string and one as a list please feel
#free to use whichever works better

    ##As a list
    # lFinalList = []
    # lFinalList.append = [sHomeTeam, iHomeScore, sOutcome]
    # lFinalList.append = [sVisitingTeam, iVisitorScore, sOutcomeVisit]
    # return lFinalList

    ##As a string
    #return (f"{sHomeTeam} score: {iHomeScore}\n{sVisitingTeam} score: {iVisitorScore}\nOutcome: {sOutcome}")

    #As a plain W or L
    return sOutcome

# game = winLoseSim("BYU", "UVU")
# print(game)

