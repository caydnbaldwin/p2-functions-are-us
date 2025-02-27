# Waylan Abbott
# Professor Greg Anderson
# Section 4
# Description: This program tracks a soccer team’s season, records match results, 
# calculates wins/losses, and evaluates overall performance based on win percentage.
import random

def main():
    # Get user input for home team name and number of games
    homeTeam = input("Enter the name of your team (the home team): ")
    numGames = int(input(f"Enter the number of games that {homeTeam} will play (1-10): "))
    
    # Dictionary to store season results
    seasonResults = {"team": homeTeam, "games": []}
    wins = 0
    
    # Loop through each game
    for gameNumber in range(1, numGames + 1):
        awayTeam = input(f"Enter the name of the away team for game {gameNumber}: ")
        
        # Generate scores until there is no tie
        homeScore = random.randint(0, 10)
        awayScore = random.randint(0, 10)
        while homeScore == awayScore:
            homeScore = random.randint(0, 10)
            awayScore = random.randint(0, 10)
        
        # Determine if it's a win or loss
        result = "W" if homeScore > awayScore else "L"
        if result == "W":
            wins += 1
        
        # Store game details in dictionary
        seasonResults["games"].append({
            "awayTeam": awayTeam,
            "homeScore": homeScore,
            "awayScore": awayScore,
            "result": result
        })
    
    # Display the results of each game
    print("\nGame Results:")
    for game in seasonResults["games"]:
        print(f"{seasonResults['team']} {game['homeScore']} - {game['awayTeam']} {game['awayScore']} ({game['result']})")
    
    # Calculate and display final record
    losses = numGames - wins
    print(f"\nFinal season record: {seasonResults['team']} {wins}-{losses}")
    
    # Determine final message based on performance
    winPercentage = wins / numGames
    if winPercentage >= 0.75:
        print("Qualified for the NCAA Women's Soccer Tournament")
    elif winPercentage >= 0.50:
        print("You had a good season")
    else:
        print("Your team needs to practice!")

# Run the program
if __name__ == "__main__":
    main()