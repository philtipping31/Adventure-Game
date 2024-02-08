import time
from os import system, name
from colorama import Fore, Style

# The backpack is your inventory for collecting items in the mansion.
backpack = []

# Global Variables

global hammer
hammer = False
global key
key = False
global blueprints
blueprints = False
global code
code = False

# note details found in the dining hall

note = {
        "home": "The Haunted Mansion",
        "owner_name": "Dr S Cary",
        "spare_key": "Safe",
        "mansion_blueprints": "Enclosed"
    }


def intro():
    """
    Displays the game intro and sets the scene.
    """
    time.sleep(2)
    print("It's a dark and cold night, you are lost and alone...\n")
    time.sleep(2)
    print("You feel as if you are being watched...\n")
    time.sleep(2)
    print("Scared! You turn and run...\n")
    time.sleep(2)
    print("You're now being chased through the dark forest...\n")
    time.sleep(2)
    print("You see a door ahead, you run in to hide...\n")
    time.sleep(2)
    print("You have entered...\n")
    time.sleep(3)
    print("         /\\     /\\")
    print("     ____||_____||____")
    print("    /                 \\")
    print("   /                   \\")
    print("  /_____________________\\")
    print("  | The Haunted Mansion!|")
    print("  |                     |")
    print("  |     ____     ___    |       0")
    print("  |    | .  |   |___|   |      /|\\")
    print("__|____|____|___________|______/ \\")
    print("")
    time.sleep(2)
    print("You look around and realise...\n")
    time.sleep(2)
    print("YOU ARE LOCKED IN!!!\n")
    time.sleep(2)
    print("Your mission is to escape the mansion or accept your fate.\n")
    time.sleep(2)
    print("")
    print("GAME OBJECTIVE\n")
    print("")
    print("Navigate through the mansion and search for clues.\n")
    time.sleep(1)
    print("Pick and choose from the options and explore the rooms.\n")
    time.sleep(1)
    print("You will face decisions throughout the mansion...\n")
    print("but be careful...\n")
    print("your decisions will affect the route of the game.\n")
    time.sleep(2)
    print("Locate the clues and items to find a way to escape.\n")
    time.sleep(2)
    print("GOOD LUCK!\n")
    time.sleep(4)
    start_game()


def start_game():
    """
    Starts the Haunted Mansion game, asking the user whether
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
            print("Incorrect input. Please type 'yes' or 'no'.\n")
            continue


def hallway():
    """
    Tells the user after clicking 'Yes' that they are in the hallway
    of the mansion.
    Provides input options for room for the user to choose from
    to progress through the mansion.
    If an incorrect option is chosen options display again.
    """
    print("\nYou are standing in the main hallway...\n")
    time.sleep(1)
    print("There are 5 doors for you to choose from...\n")
    print("... or do you take the stairs?")
    print("")
    time.sleep(2)
    print("1. A door to the kitchen")
    print("2. A door to the ballroom")
    print("3. A door to the library")
    print("4. A door to the dining hall")
    print("5. A door to the office")
    print("6. The stairs to the top floor")
    print("")
    time.sleep(2)
    while True:
        chooseRoute = input("What route do you choose?\n"
                            "\nPlease type a number between 1 to 6\n> ")
        if chooseRoute == "1":
            print("\nYou chose option 1 - Kitchen\n")
            kitchen()
            break
        elif chooseRoute == "2":
            print("\nYou chose option 2 - Ballroom\n")
            ballroom()
            break
        elif chooseRoute == "3":
            print("\nYou chose option 3 - Library\n")
            library()
            break
        elif chooseRoute == "4":
            print("\nYou chose option 4 - Dining Hall\n")
            dining_hall()
            break
        elif chooseRoute == "5":
            print("\nYou chose option 5 - Office\n")
            office()
            break
        elif chooseRoute == "6":
            print("\nYou chose option 6 - Staircase\n")
            stairs()
            break
        else:
            print(Fore.RED + "\nIncorrect input. Please choose a number"
                  " between 1 and 6\n")
            print(Style.RESET_ALL)
            continue


def kitchen():
    """
    Called when the user selects option 1 - Kitchen.
    If the user has been here before and collected the item they
    will be taken back to the hallway.
    If the user has not entered kitchen_continue will be called.
    """
    if hammer is True:
        print("You've already collected the item from this room\n")
        time.sleep(2)
        print("Go back to the hallway and choose a different door\n")
        time.sleep(2)
        hallway()
    else:
        kitchen_continue()


def kitchen_continue():
    """
    Continues from the kitchen function if the user has not entered
    this room before.
    Provides user with options a and b to choose from.
    Option a adds hammer to users backpack and they will then go
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
            print("\nYou chose to open the cupboard, inside you find a"
                  " hammer.\n Put this in your backpack as it may come"
                  " in useful later.\n")
            time.sleep(1)
            print("""
            ┌──────┐
            │      │
            │      ├────────┬─┬──┬─┐
            │      ├────────┘─┘──┘─┘
            │      │
            └──────┘""")
            time.sleep(2)
            backpack.append("Hammer")
            print("Backpack:")
            print(backpack)
            global hammer
            hammer = True
            time.sleep(3)
            print("\nYou wisely decide to ignore temptation and"
                  " leave the shiny box\n")
            print("You go back to the hallway to choose another door\n")
            hallway()
            break
        elif option == "b":
            print("\nYou chose to pick up the shiny box...\n"
                  "This was a hidden lever that opens a trap door,"
                  " you fall down the trap door to your painful death.\n")
            time.sleep(1)
            print("Bad luck!\n")
            print("You have been consumed by THE HAUNTED MANSION!\n")
            time.sleep(2)
            play_again()
        else:
            print("\nIncorrect input. Please choose option a or b\n")
            continue


def ballroom():
    """
    Called when the user selects option 2 - Ballroom.
    Sets the scene for the ballroom then calls the
    ballroom_continue function if key is not in their backpack.
    If the key is true (in backpack) the user will be told they
    have already visited this room and takes them back to the hallway
    calling the hallway function.
    """
    if key is True:
        print("You've already collected the item from this room\n")
        time.sleep(2)
        print("Go back to the hallway and choose a different door\n")
        time.sleep(2)
        hallway()
    else:
        print("You have entered the mansions Ballroom...\n")
        time.sleep(1)
        print("As you step into the ballroom you take a moment to think...\n")
        time.sleep(1)
        print("The room is huge and has no light...\n")
        time.sleep(1)
        print("You can't see a thing.\n")
        time.sleep(1)
        print("You stretch your arms out to see if you can feel anything.\n")
        time.sleep(1)
        print("You get on your hands and knees and begin searching for "
              "anything of use.\n")
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
                       "c) Search Straight Ahead\n> ")
        if option == "a":
            print("\nYou chose to search Left\n")
            time.sleep(1)
            print("You feel a metallic item under your hands\n")
            time.sleep(1)
            print("It's a KEY! This could be really useful\n")
            print("""
            ┌──────┐
            │|----|│
            │|    |├────────┬─┬──┬─┐
            │|----|│        │ ├──┤ │
            └──────┘        └─┘  └─┘
                  """)
            time.sleep(1)
            backpack.append("Key")
            print("Backpack:")
            print(backpack)
            global key
            key = True
            time.sleep(3)
            print("\nYou search for the door to try the key\n")
            time.sleep(2)
            print("You somehow locate the door and try the key\n")
            time.sleep(2)
            print("IT WORKS!\n")
            time.sleep(2)
            print("You escaped the ballroom and the hidden beast inside\n")
            time.sleep(2)
            hallway()
        elif option == "b":
            print("\nYou chose to search Right\n")
            time.sleep(2)
            print("You aimlessly search around the floor and try "
                  "to find something to help\n")
            time.sleep(2)
            print("You find nothing but cobwebs\n")
            time.sleep(2)
            print("Go back and choose a different direction\n")
            time.sleep(1)
            ballroom_continue()
        elif option == "c":
            print("\nYou chose to search straight ahead\n")
            time.sleep(2)
            print("You suddenly see a pair of white eyes, staring "
                  "straight at you..\n")
            time.sleep(2)
            print("You turn and run for in the direction of the door\n")
            time.sleep(2)
            print("The beast is two quick and grabs you\n")
            time.sleep(2)
            print("You have been eaten alive\n")
            time.sleep(1)
            print("Bad luck!\n")
            print("You have been consumed by THE HAUNTED MANSION!\n")
            time.sleep(2)
            play_again()
        else:
            print("\nIncorrect input, please choose: a, b or c\n")
            continue


def library():
    """
    Called when user selects option 3 - Library.
    Checks if code is True. If true, tells the user
    they have already been in this room.
    If they have no code, calls library_continue function.
    """
    if code is True:
        print("You've already collected the item from this room\n")
        time.sleep(2)
        print("Go back to the hallway and choose a different door\n")
        time.sleep(2)
        hallway()
    else:
        library_continue()


def library_continue():
    """
    Called when user enters library and does not have
    the code in their backpack.
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
    time.sleep(2)
    print("Luckily, vision is clear in this room as it's"
          " illuminated by candle light\n")
    time.sleep(2)
    print("You search the room for clues or something useful\n")
    time.sleep(2)
    print("The room is full of books but you notice a particular "
          "book that sticks out from the rest\n")
    time.sleep(2)
    print("There is also a locked crate on a table in the "
          "center of the room\n")
    time.sleep(2)
    print("Do you investigate or leave the library?\n")
    print("You wait a few seconds to think...\n")
    time.sleep(2)
    print("1. Pick the book up from the bookshelf\n")
    time.sleep(1)
    print("2. Attempt to get into the locked crate\n")
    time.sleep(1)
    print("3. Leave the library\n")
    time.sleep(1)
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
                print("\nYou chose option 1...\n")
                time.sleep(2)
                print("You go to grab the book but it acts like a lever...\n")
                time.sleep(2)
                print("A hidden door appears from behind the bookshelf...\n")
                time.sleep(2)
                print("Being inquisitive you walk through the door...\n")
                dining_hall()
            elif options == 2:
                print("\nYou chose option 2\n")
                time.sleep(2)
                print("The crate is tough and made of solid wood\n")
                time.sleep(2)
                print("There's no way of getting into this.\n")
                time.sleep(2)
                print("Maybe you can find something in the mansion to "
                      "help you get into this\n")
                time.sleep(2)
                print("Annoyed, you leave the library in search of an item "
                      "to help get into the crate\n")
                time.sleep(2)
                hallway()
            elif options == 3:
                print("\nYou chose option 3\n")
                time.sleep(2)
                print("You have left the library and leave all "
                      "possible help behind\n")
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
                print("Bad luck!\n")
                print("You have been consumed by THE HAUNTED MANSION!\n")
                time.sleep(2)
                play_again()
            elif options == 4 and hammer is True:
                print("\nYou smash the crate open\n")
                time.sleep(2)
                print("Inside you see tiny ripped up pieces of paper\n")
                time.sleep(2)
                print("You soon realise there are some numbers written "
                      "on the pieces\n")
                time.sleep(2)
                print("You match them all together and it reads:\n "
                      " ACCESS CODE: 7462\n")
                global code
                code = True
                time.sleep(2)
                print("You jump with joy thinking this could help you escape. "
                      "However, you accidentally knock over the candles and"
                      " the paper burns to ashes...\n")
                time.sleep(2)
                print("Hopefully you can remember this code for later...\n")
                time.sleep(7)
                clear_display()
                print("You go back to hallway to look for a possible "
                      "way out...\n")
                hallway()
            else:
                print(f"\nIncorrect input. Please choose {decisions}.\n")
                continue
        except ValueError:
            print(f"\nIncorrect input. Please choose {decisions}.\n")
            continue


def dining_hall():
    """
    Called when user selects option 4 - Dining Hall.
    If user has already collected the items from this room, the user
    will be sent back to the hallway.
    If user has not entered the room, dining_hall_continue is called.
    """
    if blueprints is True:
        print("You have already collected the items from this room\n")
        time.sleep(2)
        print("Go back to the hallway and choose a different room\n")
        time.sleep(2)
        hallway()
    else:
        dining_hall_continue()


def dining_hall_continue():
    """
    Called if user has not entered the dining hall
    and collected the item.
    In this room the note and floorplan will display
    user will be given a choice to take items or leave them.
    If they choose 'a' to take the items then this will append
    the details to the backpack and be set as true in global scope.
    If they choose 'b' this will leave the items and take the user
    back to the hallway.
    User will not lose the game in this room and will be sent back
    to the hallway to continue their search either way.
    If incorrect input, user will be asked question again.
    """

    print("You have entered the mansions Dining Hall\n")
    time.sleep(2)
    print("The dining hall is illuminated by a candle stick "
          "in the center of the table.\n")
    time.sleep(2)
    print("You see a folder named 'Owners Manual'.\n")
    time.sleep(2)
    print("You open the folder, but the pages are old and worn\n")
    time.sleep(2)
    print("One loose page falls out, you bend down and pick it up\n")
    time.sleep(2)
    print("The page is ripped and the words are faded, but you"
          " manage to work out what they read:\n")
    time.sleep(2)
    print("")
    building = note["home"]
    print(building)
    name = note["owner_name"]
    print(name)
    location = note["spare_key"]
    print(location)
    floorplan = note["mansion_blueprints"]
    print(floorplan)
    time.sleep(1)
    print("\n")
    time.sleep(3)
    print("What does this mean?...\n")
    time.sleep(2)
    print("There seems to be something missing here...\n")
    time.sleep(2)
    print("You search the folder and find another ripped page\n")
    time.sleep(2)
    print("It reads:\n")
    for key in note:
        print(key)
    print("")
    print("You line the two pieces of paper together and it reads...\n")
    time.sleep(2)
    print("Home: The Haunted Mansion")
    print("Owner: Dr S Cary")
    print("Spare Key: Safe")
    print("Mansion Blueprints: Enclosed")
    time.sleep(3)
    print("")
    print("This could be really helpful...\n")
    time.sleep(2)
    print("You search the papers on the floor for the blueprints\n")
    time.sleep(3)
    print("You find them! But only for the ground floor...\n")
    time.sleep(3)
    print(" -------------------------------------------------- ")
    print("|                                                  |")
    print("|                    Ballroom                      |")
    print("|                                                  |")
    print("|----------------------    ------------------------|")
    print("|                 |           |                    |")
    print("|                 |    |  |   |                    |")
    print("|     Office      |    |  |   |       Library      |")
    print("|                /      S     |                    |")
    print("|                 |     T      \\                   |")
    print("|                 |     A     |                    |")
    print("|-----------------|     I     |--------------------|")
    print("|                 |     R     |                    |")
    print("|                 |     S     |                    |")
    print("|                 |           |                    |")
    print("|     Kitchen    /             \\    Dining Hall    |")
    print("|                 |           |                    |")
    print("|                 |           |                    |")
    print("|----------------------    ------------------------| ")
    print("")
    while True:
        choice = input("Do you:\na) Take the letter and blueprints\n"
                       "b) Decide they are of no use and leave them"
                       " behind.\n> ")
        if choice == "a":
            backpack.append("Mansion Details")
            print("Backpack:")
            print(backpack)
            global blueprints
            blueprints = True
            print("")
            print("\nYou go back to the hallway in search for the safe with "
                  "the spare key")
            hallway()
        if choice == "b":
            print("\nYou leave them behind. You can always come back for"
                  " these\n")
            print("You head back to the hallway")
            hallway()
        else:
            print("\nIncorrect input. Please type 'a' or 'b'\n")
            continue


def office():
    """
    Called when user selects option 5 - Office.
    If incorrect input, user will be notified and given choice again.
    """
    print("You have entered the mansions office\n")
    time.sleep(1)
    print("You scan the room to look for something useful\n")
    time.sleep(2)
    print("You search for items on the desk but nothing seems to be "
          "of any use\n")
    time.sleep(2)
    print("You sit in the chair and look around again\n")
    time.sleep(2)
    print("There's a strange hatch on the wall!\n")
    time.sleep(2)
    print("Do you...\n")
    print("a) Ignore it and leave the office.\n")
    print("b) Open the hatch\n")
    time.sleep(2)
    while True:
        decision = input("Please type 'a' or 'b':\n> ")
        if decision == "a":
            print("\nYou leave the office and ignore temptation")
            time.sleep(2)
            hallway()
        elif decision == "b":
            print("\nYou open the hatch and see a safe!")
            time.sleep(2)
            break
        else:
            print("\nIncorrect input. Please type 'a' or 'b'")
            continue
    print("\nYou have another decision to make...\n")
    time.sleep(2)
    while True:
        print("Do you...\n")
        time.sleep(2)
        print("1. Do nothing, you don't know the code to get in!\n")
        time.sleep(2)
        print("2. Have a guess and see if you can guess the code.\n")
        time.sleep(2)
        if code is True:
            print("3. Remember the code from earlier and type this in!\n")
        time.sleep(2)
        if code is True:
            option = "(1, 2 or 3)"
        else:
            option = "(1 or 2)"
        try:
            options = int(input(f"Which do you choose? {option}:\n> "))
            if options == 1:
                print("\nYou chose option 1...\n")
                time.sleep(2)
                print("How could you possibly guess this code...\n")
                time.sleep(2)
                print("You leave the office in search for a code for "
                      "the safe\n")
                time.sleep(2)
                hallway()
            elif options == 2:
                print("\nYou chose option 2\n")
                time.sleep(2)
                print("Gambling your fate you enter some numbers in\n")
                time.sleep(2)
                numbers = input("Type your access code here: ")
                time.sleep(2)
                print("\nACCESS DENIED\n")
                time.sleep(2)
                print("The floor beneath you disappears in a flash\n")
                time.sleep(2)
                print("You have fallen to your death.\n")
                time.sleep(3)
                print("Bad luck!\n")
                print("You have been consumed by THE HAUNTED MANSION!\n")
                time.sleep(2)
                play_again()
            elif options == 3 and code is True:
                print("\nDo you remember the code from the ripped up pieces"
                      " of paper in the Library\n")
                time.sleep(2)
                print("You carefully type them in...\n")
                time.sleep(2)
                correct_code = input("Type in your code:\n> ")
                if correct_code == "7462":
                    print("You remembered it correctly!!\n")
                    time.sleep(2)
                    print("ACCESS GRANTED\n")
                    time.sleep(2)
                    print("The safe opens and there you see...\n")
                    time.sleep(2)
                    print("The spare key!\n")
                    time.sleep(2)
                    print("You grab the key and run to the front door!\n")
                    time.sleep(2)
                    print("IT WORKS!\n")
                    time.sleep(2)
                    game_win()
                else:
                    print("code incorrect, please try again.")
                    continue
            else:
                print(f"\nIncorrect input. Please choose {option}.\n")
                continue
        except ValueError:
            print(f"\nIncorrect input. Please choose {option}.\n")
            continue


def stairs():
    """
    Called when user selects option 6 - Staircase.
    This ends the game and is not an interactive room.
    play_again function will be called for the user try again.
    """
    print("\nYou decided to take the stairs\n")
    time.sleep(1)
    print("You've left all rooms unsearched...\n")
    time.sleep(2)
    print("You hear heavy breathing and footsteps...\n")
    time.sleep(2)
    print("In a panic you sprint up the stairs...\n")
    print("The staircase is old and brittle and a snaps underneath you\n")
    time.sleep(2)
    print("You are caught by the ghostly figure chasing you and fall to "
          "a painful death\n")
    time.sleep(2)
    print("Bad luck!\n")
    print("You have been consumed by THE HAUNTED MANSION!\n")
    time.sleep(2)
    play_again()


def play_again():
    """
    Called when the player says no to playing the game
    as well as when the player wins or dies.
    Asks user whether they would like to play again.
    If not, game ends. If Yes, intro function is called again.
    """
    while True:
        play_again = input("Would you like to play again? (yes/no):\n> ")
        if play_again == "yes":
            backpack.clear()
            global hammer
            hammer = False
            global key
            key = False
            global blueprints
            blueprints = False
            global code
            code = False
            clear_display()
            intro()
            break
        elif play_again == "no":
            print("\nNever mind... Thanks for playing and come back soon!\n")
            end_game()
        else:
            print("Incorrect input. Please type 'yes' or 'no'.")
            continue


def game_win():
    """
    Called if the player enters the correct code into the safe.
    Player escapes The Haunted Mansion!
    Play again will be called at the end of function to allow
    user the choice to play again.
    """
    print("Congratulations! You escaped the Haunted Mansion\n")
    print("Thanks for playing, come back soon.")
    time.sleep(3)
    end_game()


def end_game():
    """
    Called when player does not want to play the game again.
    clears the display but still gives user option to play again.
    """
    time.sleep(5)
    clear_display()
    play_again()


def clear_display():
    """
    Clears the console.
    """
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')


intro()
