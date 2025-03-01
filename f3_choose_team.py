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
    for i, team in enumerate(available_teams):
        print(f"[{i + 1}] {team}")

    # Get user input
    selected_team = int(input("Please select from the list by entering the desired team's number (i.e., '1'): "))

    # Return selected team
    return available_teams[selected_team - 1]