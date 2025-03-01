
#Anders Houghton
#Recieve home team, count W and L and print out record
#Function5


# Create Function and receive in home team and the amount of W's and l's

def finalrecord(homeTeam, results) :

    # Store and count W and L in variables

    wins = results.count("W")
    losses = results.count("L")
    
    #print final record 

    print(f"\nFinal Record for {homeTeam}: {wins}-{losses} (W-L)")

