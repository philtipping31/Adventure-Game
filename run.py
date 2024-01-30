import time

# The backpack is your inventory for collecting items in the mansion.
backpack = []


def intro():
    """
    Displays the game intro and sets the scene.
    """
    print("         /\\    /\\")
    print("     ___| |____| |____")
    print("    /                 \\")
    print("   /     Welcome to    \\")
    print("  /_____________________\\")
    print("  | The Haunted Mansion!|")
    print("  |                     |")
    print("  |     ____     ___    |       0")
    print("  |    | .  |   |___|   |      /|\\")
    print("__|____|____|___________|______/ \\")
    print("")
    time.sleep(1)
    print("Welcome to the Haunted Mansion\n")
    time.sleep(1)
    print("It's a dark and cold night, you are alone and scared...\n")
    time.sleep(1)
    print("You look around and realise...\n")
    time.sleep(2)
    print("YOU ARE LOCKED IN!!!\n")
    time.sleep(1)
    print("Your mission is to escape or accept your fate.\n")
    time.sleep(2)
    start_game()


def start_game():
    """
    Starts the Haunted mansion game, asking the user whether
    they want to try and escape or accept their fate.
    If they do not want to escape, the game ends.
    If yes, the game continues.
    If incorrect input is provided, the user is asked the question again.
    """

    while True:
        escape_mansion = input("Would you like to attempt your escape"
                               " from the HAUNTED MANSION? (yes/no):\n> ")
        if escape_mansion == "no":
            print("\nYou have accepted your fate...\n")
            time.sleep(1)
            print("Enjoy your stay at the HAUNTED MANSION!\n")
            time.sleep(1)
            play_again()
            break
        elif escape_mansion == "yes":
            hallway()
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
            continue


def hallway():
    """
    Tells the user after clicking 'Yes' that they are in the hallway
    of the mansion.
    Provides input options to the user to choose from to progress
    through the mansion.
    If incorrect option is chosen options display again.
    """
    print("\nYou are standing in the main hallway...\n")
    time.sleep(1)
    print("There are 5 doors for you to choose from...")
    print("... or do you take the stairs?")
    print("")
    time.sleep(1)
    print(" - A door to the kitchen (1),")
    print(" - A door to the ballroom (2),")
    print(" - A door to the library (3),")
    print(" - A door to the dining hall (4),")
    print(" - A door to the office (5),")
    print(" - The stairs to the top floor (6).")
    print("")
    time.sleep(1)
    while True:
        chooseRoute = input("What route do you choose? (1 to 6)\n> ")
        if chooseRoute == "1":
            print("You chose option 1 - Kitchen\n")
            kitchen()
            break
        elif chooseRoute == "2":
            print("You chose option 2 - Ballroom\n")
            break
        elif chooseRoute == "3":
            print("You chose option 3 - Library\n")
            break
        elif chooseRoute == "4":
            print("You chose option 4 - Dining Hall\n")
            break
        elif chooseRoute == "5":
            print("You chose option 5 - Office\n")
            break
        elif chooseRoute == "6":
            print("You chose option 6 - Staircase\n")
            break
        else:
            print("Invalid input. Please choose a number between 1 and 6")
            continue
        

def kitchen():
    """
    Called when user selects option 1 - Kitchen.
    Displays new room info text and options a and b for user to select.
    If incorrect input, user will be notified and given choice again.
    """
    time.sleep(2)
    print("You have entered the mansions kitchen...\n")
    time.sleep(1)
    print("You scan the room to see if there is anything of use\n")
    time.sleep(1)
    print("You see a closed cupboard on the wall and also notice "
          "a shiny box on the floor...\n")
    time.sleep(1)
    while True:
        option = input("Do you:\n a) Open the cupboard door \n"
                       " b) Pick up the shiny box\n>")
        if option == "a":
            print("You chose to open the cupboard, inside you find a"
                  " hammer. Put this in your backpack as it may come "
                  "in useful later\n")
            backpack.append("Hammer")
            print("Backpack:")
            print(backpack)
            time.sleep(1)
            print("You wisely decide to ignore temptation and"
                  " leave the shiny box")
            print("You go back to the hallway to choose another door")
            hallway()
            break
        elif option == "b":
            print("You chose to pick up the shiny box...\n"
                  " This was a hidden lever that opens a trap door,"
                  " you fall down the trap door to your painful death\n")
            time.sleep(1)
            print("Bad luck.\n"
                  "You have been consumed by THE HAUNTED MANSION!\n")
            play_again()
        else:
            print("Invalid input. Please choose option a or b")
            continue


def ballroom():
    """
    Called when user selects option 2 - Ballroom.
    Displays new room info text and options a and b for user to select.
    If incorrect input, user will be notified and given choice again.
    """


def library():
    """
    Called when user selects option 3 - Library.
    Displays new room info text and options a and b for user to select.
    If incorrect input, user will be notified and given choice again.
    """


def dining_hall():
    """
    Called when user selects option 4 - Dining Hall.
    Displays new room info text and options a and b for user to select.
    If incorrect input, user will be notified and given choice again.
    """


def office():
    """
    Called when user selects option 5 - Office.
    Displays new room info text and options a and b for user to select.
    If incorrect input, user will be notified and given choice again.
    """


def stairs():
    """
    Called when user selects option 6 - Staircase.
    Displays new room info text and options a and b for user to select.
    If incorrect input, user will be notified and given choice again.
    """


def play_again():
    """
    Called when the player says no to playing the game
    as well as when the player wins or dies.
    Asks user whether they would like to play again. 
    If not, game ends. If Yes, intro function is called again.
    """
    while True:
        play_again = input("Would you like to play again? (yes/no):\n")
        if play_again == "yes":
            backpack.clear()
            intro()
            break
        elif play_again == "no":
            print("\nNever mind... Thanks for playing and come back soon!\n")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
            continue


intro()