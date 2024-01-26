import time

# Global variables
global lighter
lighter = "no"
global backpack
backpack = "no"


def intro():
    """
    Displays the game intro and sets the scene.
    """
    print("        /\\     /\\")
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
                                "from the HAUNTED MANSION? (yes/no):\n")
        if escape_mansion == "no":
            print("\nYou have accepted your fate...\n")
            time.sleep(1)
            print("Enjoy your stay at the HAUNTED MANSION!\n")
            time.sleep(1)
            print("GAME OVER\n")
            play_again()
            break
        elif escape_mansion == "yes":
            choose_item()
            break
        else:
            print("Wrong input. Please type 'yes' or 'no'.")
            continue


intro()