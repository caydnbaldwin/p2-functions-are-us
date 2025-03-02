# Aaron McCoy, Anders Houghton, Caydn Baldwin, George Martinez, Ryan Bartholomew, Waylan Abbott
# IS 303 Section 4
# P2 - Functions Are Us
# A program that plays the women’s soccer season as defined in Assignment 4.

import f1_introduction
import f2_menu
import f3_choose_team
import f4_wins_losses
import f5_print_final_record

# main function
def main():
    # 1
        # Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message. Return the name to the main program and store it in variable so it can be used throughout the program.
    coach_name = f1_introduction.display_intro()
    # 2
        # Display of menu and return choice. Store in variable and use this value to determine which function to call next.
    main_menu_item = f2_menu.display_menu()
    while main_menu_item != 3:
        if main_menu_item == 1: # Choose your team to begin the season
            home_team = f3_choose_team.choose_sports_team()
            number_of_games = int(input("\nEnter the number of games that your team will play in their season: "))
            # initialize other necessary variables
            schedule = {}
            record = []
            print("\nTraveling back to main menu. You should select to `[2] Start season.` next.")
            main_menu_item = f2_menu.display_menu()

        elif main_menu_item == 2: # Start season
            for game_number in range(1, number_of_games + 1):
                away_team = f3_choose_team.choose_sports_team(home_team)
                result, home_score, away_score = f4_wins_losses.winLoseSim(home_team, away_team)
                schedule[game_number] = [home_team, home_score, away_team, away_score, result]
                record += result
            
            print("\nTraveling back to main menu. You should select to `[3] Display the final record of the season.` next.")
            main_menu_item = f2_menu.display_menu()

    else: # Display the final record
        print()
        for game in schedule:
            print(f"{schedule[game][4]} -> {schedule[game][0]}'s score: {schedule[game][1]} {schedule[game][2]}'s score: {schedule[game][3]}")
        f5_print_final_record.finalrecord(home_team, record)
        print()

    win_percentage = record.count("W") / len(record)
    if win_percentage >= 0.75:
        print(f"{coach_name}, your team qualified for the NCAA Women's Soccer Tournament!")
    elif win_percentage >= 0.5:
        print(f"{coach_name}, you had a good season.")
    else:
        print(f"{coach_name}, your team needs to practice!")

    print()

# check if script is run directly as the main program, then execute `main()`
if __name__ == "__main__":
    main()