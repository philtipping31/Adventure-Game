import time

# The backpack is your inventory for collecting items in the mansion.
backpack = []

# Global Variables

global hammer
hammer = False
global key
key = False


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
            ballroom()
            break
        elif chooseRoute == "3":
            print("You chose option 3 - Library\n")
            library()
            break
        elif chooseRoute == "4":
            print("You chose option 4 - Dining Hall\n")
            dining_hall()
            break
        elif chooseRoute == "5":
            print("You chose option 5 - Office\n")
            office()
            break
        elif chooseRoute == "6":
            print("You chose option 6 - Staircase\n")
            stairs()
            break
        else:
            print("Invalid input. Please choose a number between 1 and 6")
            continue
        

def kitchen():
    """
    Called when user selects option 1 - Kitchen.
    If user has been here before and collected the item they 
    will be taken back to the hallway.
    If the user has not entered kitchen_continue will be called.
    """
    if hammer is True:
        print("You've already collected the item from this room\n")
        print("Go back to hallway and choose a different door")
        hallway()
    else:
        kitchen_continue()


def kitchen_continue():
    """
    Continues from the kitchen function if user has not entered
    this room before.
    Proivdes user with options a and b to choose from.
    If a or b are not entered, invalid error appears and choices
    are given again.
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
            global hammer
            hammer = True
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
    Sets the scene for the ball room the calls the
    ballroom_continue function.
    """
    if key is True:
        print("You've already collected the item from this room\n")
        print("Go back to hallway and choose a different door")
        hallway()
    else:
        print("You have entered the mansions Ballroom...\n")
        time.sleep(1)
        print("As you step into the ballroom you take a moment to think...\n")
        time.sleep(1)
        print("The room is huge and has no light...\n")
        time.sleep(1)
        print("You can't see a thing\n")
        time.sleep(1)
        print("You stretch your arms out to see if you can feel anything.\n")
        time.sleep(1)
        print("You get on your hands and knees and begin searching for "
              "anything of use")
        time.sleep(1)
        print("However, you have a decision to make...")
        ballroom_continue()
        

def ballroom_continue():
    while True:
        option = input("Do you:\na) Search Left\nb) Search Right\n"
                       "c) Search Straight Ahead\n>")
        if option == "a":
            print("You chose to search Left")
            print("You feel a metallic item under your hands")
            print("It's a KEY! This could be really useful")
            backpack.append("Key")
            print("Backpack:")
            print(backpack)
            global key
            key = True
            print("You search for the door to try the key")
            print("You somehowe locate the door and try the key")
            print("IT WORKS!")
            print("You escaped the ballroom and the hidden beast inside")
            hallway()
        elif option == "b":
            print("You chose to search Right")
            print("You aimless search around the floor and try "
                  "to find something to help")
            time.sleep(2)
            print("You find nothing but cobwebs")
            print("Go back and choose a different direction")
            ballroom_continue()
        elif option == "c":
            print("You chose to search straight ahead")
            print("You suddenly see a pair of white eyes, staring "
                  "straight at you..")
            print("You turn and run for in the direction of the door")
            print("The beast is two quick and grabs you")
            print("You have been eaten alive")
            print("Bad luck\n")
            print("You have been consumed by THE HAUNTED MANSION")
            play_again()
        else:
            print("Invalid input, please choose: a, b or c")
            continue


def library():
    """
    Called when user selects option 3 - Library.
    If incorrect input, user will be notified and given choice again.
    """
    print("You have entered the mansions Library\n")
    time.sleep(1)
    print("You search the room for clues or something useful\n")


def dining_hall():
    """
    Called when user selects option 4 - Dining Hall.
    If incorrect input, user will be notified and given choice again.
    """
    print("You have entered the mansions Dining Hall")


def office():
    """
    Called when user selects option 5 - Office.
    If incorrect input, user will be notified and given choice again.
    """
    print("You have entered the mansions office")


def stairs():
    """
    Called when user selects option 6 - Staircase.
    This ends the game and is not an interactive room.
    play_again function will be called for the user try again.
    """
    print("You decided to take the stairs\n")
    print("You've left all rooms unsearched...\n")
    time.sleep(1)
    print("You hear heavy breathing and footsteps...\n")
    time.sleep(1)
    print("In a panic you sprint up the stairs...\n")
    print("The staircase is old and brittle and a snaps underneath you\n")
    time.sleep(1)
    print("You are caught by the ghostly figure chasing you and fall to "
          "a painful death")
    time.sleep(1)
    print("Bad luck.\n"
          "You have been consumed by THE HAUNTED MANSION!\n")
    play_again()


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