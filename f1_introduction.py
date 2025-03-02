# Waylan Abbott
# Function 1
# Displays an introduction to the game explaining rules and prompt for their name and display that in the welcome message

def display_intro():

# Display game introduction, explain rules, and prompt for user's name.
    print("Welcome to the College Soccer Season Simulator!")
    print("In this game, you will coach a soccer team through a season.")
    print("You will enter your team's name, choose the number of games to play (1-4),")
    print("and input the opponents' names. Scores will be randomly generated.")
    print("Your goal is to win as many games as possible and qualify for the NCAA Tournament!\n")
    
    user_name = input("Before we start, what is your name, Coach? ")
    print(f"\nGreat to have you here, Coach {user_name}!")

    return user_name