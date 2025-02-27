# Aaron McCoy, Anders Houghton, Caydn Baldwin, George Martinez, Ryan Bartholomew, Waylan Abbott
# Section 4
# P2 - Functions Are Us
# Displays information about a soccer team utilizing OOP and loosely implementing inheritance

import random

class Team:
    # Initializes Team object by getting team name and number of games. Then initializes schedule, wins, losses, and evaluation string
    def __init__(self):
        self.team_name = input("Enter the name of your home team: ")
        self.number_of_games = int(input("Enter the number of games that your team will play in their season: "))
        self.schedule = {}
        self.wins = 0
        self.losses = 0
        self.evaluation_string = ""

    # Iterates through the number of games, creates new_game object, generates scores, updates team record, then adds the game results to the schedule dictionary 
    def iterate_through_number_of_games(self):
        for game_number in range(1, self.number_of_games + 1):
            new_game = Game(self.team_name, game_number)
            new_game.generate_scores()
            self.wins, self.losses = new_game.update_record(self.wins, self.losses)
            self.schedule[game_number] = [new_game.home_team, new_game.home_score, new_game.away_team, new_game.away_score]

    # Evaluates team win percentage, then generate a string conditioned upon the percentage
    def evaluation(self):
        win_percentage = self.wins / (self.wins + self.losses)
        if win_percentage >= 0.75:
            self.evaluation_string = "Qualified for the NCAA Women's Soccer Tournament"
        elif win_percentage >= 0.5:
            self.evaluation_string = "You had a good season."
        else:
            self.evaluation_string = "Your team needs to practice!"

    # String function to print everything relevant to the class
    def __str__(self):
        for game in self.schedule:
            print(f"{self.schedule[game][0]}'s score: {self.schedule[game][1]} {self.schedule[game][2]}'s score: {self.schedule[game][3]}")
        print(f"\nFinal season record: {self.wins} - {self.losses}")
        print(f"\n{self.evaluation_string}")

class Game:
    # Initializes Game object by inheriting home_team name, getting away_team name, and initializing scores for both teams
    def __init__(self, team_name, game_number):
        self.home_team = team_name
        self.away_team = input(f"Enter the name of the away team for game {game_number}: ")
        self.home_score = 0
        self.away_score = 0

    # randomly generates scores, rescores indefinitely until at least one team has scored and it is not a tie
    def generate_scores(self):
        while (not self.home_score > 0 or not self.away_score > 0) and (self.home_score == self.away_score):
            self.home_score = random.randint(0, 4)
            self.away_score = random.randint(0, 4)

    # updates the team record
    def update_record(self, wins, losses):
        if self.home_score > self.away_score:
            return wins + 1, losses
        else:
            return wins, losses + 1
        
# create season, iterate through games, evaluate season, print results
if __name__ == '__main__':
    season = Team()
    season.iterate_through_number_of_games()
    season.evaluation()
    season.__str__()
