import time


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
    print("  |     ____     ___    |")
    print("  |    | .  |   |___|   |")
    print("__|____|____|___________|__")
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
                                " from the HAUNTED MANSION? (yes/no):\n>")
        if escape_mansion == "no":
            print("\nYou have accepted your fate...\n")
            time.sleep(1)
            print("Enjoy your stay at the HAUNTED MANSION!\n")
            time.sleep(1)
            print("GAME OVER\n")
            play_again()
            break
        elif escape_mansion == "yes":
            hallway()
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue


def hallway():
    print("\nYou are standing in the main hallway...\n")
    time.sleep(1)
    print("There are 5 for you to choose from...")
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
    time.sleep(2)
    chooseRoute = input("What route do you choose? (1 to 6)\n>")
    if chooseRoute == "1":
        print("you chose option 1")
    elif chooseRoute == "2":
        print("you chose option 2") 
    elif chooseRoute == "3":
        print("you chose option 3")
    elif chooseRoute == "4":
        print("you chose option 4")
    elif chooseRoute == "5":
        print("you chose option 5")
    elif chooseRoute == "6":
        print("you chose option 6")
    else:
        print("Wrong input. Please choose a number between 1 and 6")


intro()