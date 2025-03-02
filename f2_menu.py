#George Martinez 
#Function 2
#Displays a menu of choice that allows the user to choose an option and continue with the program.


def display_menu():
    # Display a menu with a list of options. Then the user inputs a response and thier choice is returned. 
    print ("\nMain Menu:\n1. Choose your team to begin the season. \n2. Choose your opponet.\n3. Play a game. \n4. Display the final record of the season.")
    user_choice = input ("\nPlease select from the following options coach (1, 2, 3, or 4): ")
    return user_choice

