import time
from os import system, name

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
    Provides input options for room to the user to choose from
    to progress through the mansion.
    If incorrect option is chosen options display again.
    """
    print("\nYou are standing in the main hallway...\n")
    time.sleep(1)
    print("There are 5 doors for you to choose from...\n")
    print("... or do you take the stairs?")
    print("")
    time.sleep(1)
    print("1. A door to the kitchen")
    print("2. A door to the ballroom")
    print("3. A door to the library")
    print("4. A door to the dining hall")
    print("5. A door to the office")
    print("6. The stairs to the top floor")
    print("")
    time.sleep(1)
    while True:
        chooseRoute = input("What route do you choose?\n" 
                            "Please type a number between 1 to 6\n> ")
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
        print("Go back to hallway and choose a different door\n")
        hallway()
    else:
        kitchen_continue()


def kitchen_continue():
    """
    Continues from the kitchen function if user has not entered
    this room before.
    Proivdes user with options a and b to choose from.
    Option a adds hammer to users back pack and they will then go 
    back to the hallway.
    Option b results in game over and play_again function is called.
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
                       " b) Pick up the shiny box\n> ")
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
                  " leave the shiny box\n")
            print("You go back to the hallway to choose another door\n")
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
    ballroom_continue function if key is not in their backpack.
    If the key is true (in backpack) the user will be told they
    have already visited this room and take them back to the hallway
    calling the hallway function.
    """
    if key is True:
        print("You've already collected the item from this room\n")
        print("Go back to hallway and choose a different door\n")
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
              "anything of use\n")
        time.sleep(1)
        print("However, you have a decision to make...\n")
        ballroom_continue()
        

def ballroom_continue():
    """
    Function is called if user enters the ballroom and
    does not have the key in their backpack.
    User will be given options on what direction they wish
    to take in search for an item.
    Option a grants the user a key which will allow them
    to escape from the ballroom unharmed.
    Option b is a dead end and calls ballroom_continue
    again to allow a second choice of direction.
    Option c results in game over and play_again function
    is called.
    If any other character is entered, invalid input is shown
    and input options are asked again.
    """
    while True:
        option = input("Do you:\na) Search Left\nb) Search Right\n"
                       "c) Search Straight Ahead\n>")
        if option == "a":
            print("You chose to search Left\n")
            time.sleep(1)
            print("You feel a metallic item under your hands\n")
            time.sleep(1)
            print("It's a KEY! This could be really useful\n")
            time.sleep(1)
            backpack.append("Key")
            print("Backpack:")
            print(backpack)
            global key
            key = True
            print("You search for the door to try the key\n")
            time.sleep(1)
            print("You somehowe locate the door and try the key\n")
            time.sleep(1)
            print("IT WORKS!\n")
            time.sleep(1)
            print("You escaped the ballroom and the hidden beast inside\n")
            time.sleep(2)
            hallway()
        elif option == "b":
            print("You chose to search Right\n")
            time.sleep(1)
            print("You aimless search around the floor and try "
                  "to find something to help\n")
            time.sleep(2)
            print("You find nothing but cobwebs\n")
            time.sleep(1)
            print("Go back and choose a different direction\n")
            time.sleep(1)
            ballroom_continue()
        elif option == "c":
            print("You chose to search straight ahead\n")
            time.sleep(1)
            print("You suddenly see a pair of white eyes, staring "
                  "straight at you..\n")
            time.sleep(1)
            print("You turn and run for in the direction of the door\n")
            time.sleep(1)
            print("The beast is two quick and grabs you\n")
            time.sleep(1)
            print("You have been eaten alive\n")
            time.sleep(1)
            print("Bad luck\n")
            print("You have been consumed by THE HAUNTED MANSION\n")
            time.sleep(2)
            play_again()
        else:
            print("Invalid input, please choose: a, b or c")
            continue


def library():
    """
    Called when user selects option 3 - Library.
    User will be given 3 choices to progress with.
    Function will check if user has a hammer and add a 4th option.
    Decision options will then populate for user to choose from.
    Option 1 will end in calling the dining_room function.
    Option 2 will tell the user they need to locate an item to 
    progress and call the hallway function.
    Option 3 will result in failing the game and call the play_again
    function.
    If incorrect input, user will be notified and given choice again.
    """
    print("You have entered the mansions Library\n")
    time.sleep(1)
    print("Luckily, vision is clear in this room as it's "
          " illuminated by candle light\n")
    time.sleep(2)
    print("You search the room for clues or something useful\n")
    time.sleep(2)
    print("The room is full of books but you notice a particular "
          " book that sticks out from the rest\n")
    time.sleep(1)
    print("There is also a locked crate on a table in the "
          "center of the room\n")
    time.sleep(1)
    print("Do you investigate or leave the library?\n")
    print("You wait a few seconds to think...\n")
    time.sleep(2)
    print("1. Pick the book up from the bookshelf\n")
    print("2. Attempt to get into the locked crate\n")
    print("3. Leave the library\n")
    if hammer is True:
        print("4. Smash the crate with your hammer\n")
    time.sleep(2)
    if hammer is True:
        decisions = "(1, 2, 3 or 4)"
    else:
        decisions = "(1, 2 or 3)"
    while True:
        try:
            options = int(input(f"Which do you choose? {decisions}:\n> "))
            if options == 1:
                print("You chose option 1...\n")
                time.sleep(2)
                print("You go to grab the book but it acts like a lever...\n")
                time.sleep(2)
                print("A hidden door appears from behind the bookshelf...\n")
                time.sleep(2)
                print("Being inquisitive you walk through the door...\n")
                dining_hall()
            elif options == 2:
                print("You chose option 2\n")
                time.sleep(2)
                print("The crate is tough and made of solid wood\n")
                time.sleep(2)
                print("There's no way of getting into this.\n")
                time.sleep(2)
                print("Maybe you can find something in the mansion to "
                      "help you get into this\n")
                time.sleep(2)
                print("Annoyed, you leave the library in search of an item "
                      " to help get into the crate\n")
                time.sleep(2)
                hallway()
            elif options == 3:
                print("You chose option 3\n")
                tim.sleep(2)
                print("You have left the library and leave all "
                      " possible help behind\n")
                time.sleep(3)
                print("What a bad idea...\n")
                time.sleep(2)
                print("You are followed out by a swarm of poisionous bats\n")
                time.sleep(1)
                print("You try and run but you trip and fall...\n")
                time.sleep(1)
                print("The bats surround you and inject you with poision\n")
                time.sleep(1)
                print("You are dead in a matter of minutes\n")
                time.sleep(3)
                print("Bad Luck\n")
                print("You have been consumed by THE HAUNTED MANSION\n")
                play_again()
            elif options == 4 and hammer is True:
                print("You smash the crate open\n")
                time.sleep(2)
                print("Inside you see tiny ripped up pieces of paper\n")
                time.sleep(2)
                print("You soon realise there are some numbers written "
                      "on the pieces\n")
                time.sleep(1)
                print("You match them all together and it reads:\n "
                      " ACCESS CODE: 7462")
                print("You jump with joy thinking this could help you escape. "
                      "However, you accidentally knock over the candles and"
                      " the paper burns to ashes...\n")
                time.sleep(2)
                print("Hopefully you can remember this code for later...\n")
                time.sleep(8)
                clear_display()
                print("You go back to hallway to look for a way out...\n")
                hallway()
            else:
                print(f"Incorrect input. Please choose {decisions}.")
                continue
        except ValueError:
            print(f"Incorrect input. Please choose {decisions}.")
            continue


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
            global hammer
            hammer = False
            global key
            key = False
            clear_display()
            intro()
            break
        elif play_again == "no":
            print("\nNever mind... Thanks for playing and come back soon!\n")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
            continue


def clear_display():
    """
    Clears the console.
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


intro()