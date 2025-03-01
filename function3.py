
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
    return teams[selected_team - 1]