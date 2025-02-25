# p2-functions-are-us
As a group and using Git/Github, write a program that plays the women’s soccer season as defined in Assignment 4. Modify the code to use functions as defined below. You can do more than what is required.

## CHAPTER 9

### What is a function?

              Perform work

              Possibly return a value

 

### Syntax

              def name(parameters) :

                             Maybe return

 

### Prewritten functions:

9.2

9.3

9.4

#### 9.5

Write a program that prompts for the number of employees and then stores the user first name, user last name, hourly wage. Before storing, do the following:

    Convert the enter last name to uppercase (Capitalize)

    Replaces the string “greg” in the first name to be gary (replace)

    Convert the first character to uppercase (upper)

Prints today’s date like Tuesday February 04 and the first name, last name, hourly wage (using 2 decimals and format )

Then print all the data for each employee

#### 9.6

Random() – returns number between 0 and .9999999

import random

table 9.8

Explain Seed()

 

```
# prints a random value from the list

list1 = [1, 2, 3, 4, 5, 6]

print(random.choice(list1))

# prints a random item from the string

string = "striver"

print(random.choice(string))

print(random.randrange(1, 10)) # Can return values from 1 to 9, but never 10

```



Modify the program to generate a random rating for each employee between 0 and 10 and store that also to the list. Print all the data

 

## Chapter 11 – Writing a Function

### DO THIS FIRST and then the TUTORIAL

Eliminate duplicate code - When calling the same code over and over

Will I or someone else use this again?

```def function_name(optional_parameters) :``` 

It must begin with a letter or underscore
You may include numbers in the name
They can be of any length
WATCH OUT FOR KEY WORDS!

What is a parameter or argument?

The rules for naming a parameter are consistent with naming variables and functions.

Calling and receiving better match in position and type

You can provide a default value

```
def has_a_pet( sType = "dog", iCount = 1 ) :

RETURN 1 value for many values

def add() :

    print("Add a student")

    return "Student Added", "Johnny", "Appleseed", "Gardening"

 

# Display the return value for the add() function   

    sResult, sFirst, sLast, sHobby = add()

    print(f"The {sResult} was {sFirst} {sLast} whose hobby is {sHobby}")

print(sResult)
```

Once again, calling and receiving number of arguments must match!

STOP AT LAMBDA FOR NOW

 

## Functions

As a group and using Git/Github, write a program that plays the women’s soccer season as defined in Assignment 4. Modify the code to use functions as defined below. You can do more than what is required.

Everyone works on a Main function that calls other functions. Create the following functions:

1. Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message. Return the name to the main program and store it in variable so it can be used throughout the program.

2. Display of menu and return choice. Store in variable and use this value to determine which function to call next.

3. Display list of all teams and allow the user to choose a team using a menu. Call the function again to let the user choose the opponent but do not display the team they chose previously. Remove that team from the list. Allow the user to select an opponent, and return team name. This function should receive a parameter but give it a default value if none is passed. You can use this function for both choosing the home team and the opponent team.

4. Play the game receiving both team names. Generate random scores without ties. Return W or L.

5. Display the final record for a team. Receive the home team data and display information.

NOTE: If there are more team members than functions that need to be created then the main function can be created by one individual.