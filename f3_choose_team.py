# Aaron McCoy
# Function 3
# Display list of all teams and allow the user to choose a team using a menu. Call the function again to let the user choose the opponent but do not display the team they chose previously. Remove that team from the list. Allow the user to select an opponent, and return team name. This function should receive a parameter but give it a default value if none is passed. You can use this function for both choosing the home team and the opponent team.

def choose_sports_team(previous_choice=None):
    teams = ["BYU", "UVU", "USU",  "SUU", "UofU"]
    available_teams = teams.copy() # Create a copy to avoid modifying the original

    # Check to see if previous choice exists and is still in the team list, trash it if it is
    if previous_choice and previous_choice in available_teams:
        available_teams.remove(previous_choice)

    # Display menu
    print()
    print("Teams:")
    for i, team in enumerate(available_teams):
        print(f"[{i + 1}] {team}")

    # Get user input
    if len(available_teams) == 5:
        selected_team = int(input("\nPlease select from the list by entering the desired team's number (1, 2, 3, 4, or 5): "))
    else:
        selected_team = int(input("\nPlease select from the list by entering the desired team's number (1, 2, 3, or 4): "))

    # Return selected team
    return available_teams[selected_team - 1]