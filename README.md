# The Haunted Mansion - Text Based Adventure Game.

![Intro](docs/intro_gif.gif)

## How to Play / Game Objective

The Haunted Mansion is an easy to play Python terminal game that can be interacted with by the end user with the use of text. The project runs on the Code Institute terminal Heroku.

The objective of the game is to navigate through the Haunted Mansion and escape without dying. 

The game will first load in and set the scene, welcoming them to The Haunted Mansion.

The game objectives will shortly follow to give the end user an understanding of what they need to do.

The game will ask the user if they want to attempt to escape or accept their fate. If they choose yes, the game will continue to their first set of choices. If they choose not to escape, the game will result in the player dying. However, the option to play again will be shown. 

The user will be able to choose from 5 rooms and the stairs to explore the mansion. Each room will have some form of interaction that user will need to input via text. These options can result in a variety of outcomes and will change the direction of the game based on what is chosen.

The live link can be found here: [The Haunted Mansion - Text Based Adventure Game](https://the-haunted-mansion-d168abdc0e4f.herokuapp.com/)


## User Experience

As a first-time user I want to know the purpose of the game.

As a first-time user I want to know how to play the game. 

As a first-time user I want to be told if I have entered text incorrectly.

As a first-time user I want to be able to have the option of playing again if I do not win or even if I do win.

As a first-time user I want to know when I have lost and when I have won the game. 

As a returning user, all of the above experiences should also apply.

## Features

### Objective

The objective of the game is shown in the terminal so the user can clearly understand the purpose of the game and what they need to do.

![Objective](docs/objective.png)

### User Input

Interaction with the game is the main part of The Haunted Mansion. All rooms will require some form of interaction where a user is required to make a decision, which can result in either collecting items, moving through rooms, discovering dead ends, encountering enemies that may result in death.

![User Input](docs/user_input.png)

![User Input Rooms](docs/user_input_rooms.png)

The user will also be notified if any incorrect input has been added to the terminal.

![Incorrect input](docs/incorrect_input.png)

### Visual Features

I created visual pictures in the terminal for items that can be collected throughout the mansion.

![Hammer](docs/hammer.png)     


![Key](docs/key.png) 


![Blueprints](docs/blueprints.png)

### Backpack

The backpack is an inventory of the items the user can collect throughout the mansion. Each time an item is collected, the backpack contents will be shown to the user.

![Backpack](docs/backpack.png)

### Rooms

Rooms can be explored by the user selecting from the list when they are in the hallway. A feature is in place so that if the user has visited a room previously and collected the item, they will be told so they do not enter the room again. This will automatically send them back to the hallway to choose a different option.

![Rooms](docs/rooms.png)

![Rooms re-enter](docs/room_re_enter.png)

### Win and Loss 

The terminal will always display when a user has lost the game as well as when they win the game. After this, the user will be given the option to play again.

![Loss](docs/game_loss.png)

![Win](docs/game_win.png)

### Replay

The user will always be prompted with the play again function when the following occurs:

- Chooses not to play the game initially.
- Fails a room and dies at any point throughout.
- After winning the game.

![Play Again](docs/play_again.png)

![Play Again No](docs/no_play_again.png)



## Technologies

* Python was used as the programming language to make the game.
* [LucidChart](https://www.lucidchart.com/pages/) was used to create the flow chart showing the game's logic.
* [GitHub](https://github.com/) has been used to store the code, images, readMe file and other content. 
* [Heroku](https://dashboard.heroku.com/apps) was used to deploy the game to the browser to allow playing in a terminal.
* I used the Chrome extension [Screen Recorder](https://chromewebstore.google.com/detail/screen-recorder/hniebljpgcogalllopnjokppmgbhaden) to record the deployed terminal before converting into a gif.
* [Ezgif](https://ezgif.com/video-to-gif) was used to change video recordings into gifs for ReadME document.

### Python Modules

* Python module [time](https://docs.python.org/3/library/time.html) has been used to allow for a delay between lines of text displaying.
* Python module [Sys os](https://docs.python.org/3/library/os.html)  was used to clear the terminal display.
* Python module [Colorama](https://pypi.org/project/colorama/) was used to add coloured text in the terminal.

## Testing

### Validator Testing

The project was tested via [Code Institute's PEP8 Linter](https://pep8ci.herokuapp.com/) and returned no errors.

![Validator](docs/pep8_testing.png)

### Project Testing

All scenarios were tested locally on the CodeAnywhere terminal and then again after deployment on the Heroku App.

The below flow chart was used as a reference to ensure each function performed the correct actions based on the user's input and status.

![LucidChart](docs/workflow_chart.png)


### Functions


#### intro()


| Test                                                        | Action                                                                                                                     | Expected                                                     | Result |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------ |
| Does the intro function call when the terminal loads        | Load terminal in CodeAnywhere and Heroku. Check if intro function runs properly.                                           | Intro function calls correctly when the terminal loads       | Pass   |
| Does the intro function display all text correctly          | Load terminal in CodeAnywhere and Heroku. Check if all text shows correctly in terminal                                    | Intro function displays all text correctly in terminal       | Pass   |
| At the end of the function does start_game() call correctly | In the terminal of CodeAnywhere and Heroku when the intro function ends make sure the start game function loads correctly. | At the end of the function start_game() is called correctly. | Pass   |



#### start_game()


| Test                                                                                                                         | Action                                                                                                                           | Expected                                                                                                                   | Result |
| ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------ |
| Does start_game load in after intro()                                                                                        | Load terminal in CodeAnywhere and Heroku. Intro loads and check if start game function loads in after intro finishes             | start_game correctly shows after intro finishes.                                                                           | Pass   |
| Does the function correctly ask the user whether they want to play the game or not.                                          | Check if input section appears and allows user to type                                                                           | User can type input section on whether they want to play the game or not                                                   | Pass   |
| If user selects 'Yes' does the hallway() function correctly load                                                             | Type yes into the console and see if the hallway() function correctly loads                                                      | After typing yes, hallway() function loads in correctly                                                                    | Pass   |
| If the user selects 'No' does the text display correctly and then load the play_again function                               | Type No into the terminal. Check that the correct text displays. Check for play_again function to be callled.                    | Typing no ends the game for the user but then loads the play again function asking the user if they do want to play again. | Pass   |
| If the user enters text that is not 'yes' or 'no' does the terminal display incorrect input and ask the user to input again. | Type any other text into the input section of the terminal. Check that the error text shows and asks the user to type yes or no. | Incorrect input message shows up if anything else is entered besides, 'yes' or 'no'. The question is then asked again.     | Pass   |



#### play_again()

| Test                                                                                                                         | Action                                                                                                                                                                                                                                  | Expected                                                                                                                                                                | Result |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Does play_again load in after every time the user loses the game or chooses not to play.                                     | Load terminal in CodeAnywhere and Heroku. Using the flowchart for reference go through each scenerio where play_again() is called and check the play again function shows in terminal asking the user to input yes or no to play again. | User sees option to type yes or no to play again each time the function is called. After losing, winning the game or choosing not to play the game at the start.        | Pass   |
| Does the function correctly ask the user whether they want to play the game again or not.                                     | Check if input section appears and allows user to type. Clearly showing whether to type yes or no.                                                                                                                                      | User can type input section on whether they want to play the game again or not                                                                                          | Pass   |
| If user selects 'Yes' does the console clear correctly                                                                       | Type yes into the console and see if the intro() function correctly loads                                                                                                                                                               | After typing yes, intro() function loads in correctly                                                                                                                   | Pass   |
| If user selects 'Yes' does the backpack list clear correctly                                                                 | Type yes to play again, using the workflow for reference go into a room and collect and item to ensure backpack is empty when the item is appended to the list.                                                                         | No items from the previous playthrough have carried over and the backpack is empty. Appending newly collected items from the current playthrough                        | Pass   |
| If user selects 'Yes' do all global items reset to False                                                                     | Type yes to play again, using the workflow, go into a room with a global item. Check if you are able to enter the room as normal even if you had the item in the previous playthrough.                                                  | All rooms can be accessed as if it was the first time even after a playthrough. Functions work correctly based on global item status.                                   | Pass   |
| If user selects 'Yes' does the intro() function call correctly.                                                              | Type Yes to play again and ensure the intro function is called and runs correctly.                                                                                                                                                      | After clicking yes, console clears and game restarts running the intro() function.                                                                                      | Pass   |
| If the user selects 'No' does the text display correctly and then load the end_game function                                 | Type No into the terminal. Check that the correct text displays. Check end_game function loads after and then user will still be given the option to play again and therefore calls play_again function from the end_game function      | Typing no ends the game for the user but then loads the end_game function clearing the display and then calls play_again asking the user if they do want to play again. | Pass   |
| If the user enters text that is not 'yes' or 'no' does the terminal display incorrect input and ask the user to input again. | Type any other text into the input section of the terminal. Check that the error text shows and asks the user to type yes or no.                                                                                                        | Incorrect input message shows up if anything else is entered besides, 'yes' or 'no'. The question is then asked again.                                                  | Pass   |



#### end_game()

| Test                                                                 | Action                                                                                                       | Expected                                                                                                                                                                                    | Result |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Does end_game call when a user clicks no in the play again function. | Choose no when the play_again function is displayed                                                           | end_game should run and clear the console,finally displaying the option to play again.                                                                                                      | Pass   |
| Does end_game show after the user wins the game                      | Win the game, wait for game_win function to show and then wait for the console to clear                       | After winning the game and seeing the game_win text. The end_game function is called, clearing the display and asking user if they want to play again from calling the play_again function. | Pass   |
| Does the console clear once the end_game function is called.         | Using the workflow get to each point where end_game function is called and wait to see if the console clears | Console clears all data each time end_game is called.                                                                                                                                       | Pass   |



#### hallway()

| Test                                                                                                                                            | Action                                                                                                      | Expected                                                                                                                                     | Result |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| When called does the hallway display all options (rooms) for the user to choose from                                                            | Using workflow go through each scenario where the hallway is called to ensure the results are the same      | Hallway is called correctly and shows correct text and the rooms to choose from along with the input section                                 | Pass   |
| Does the input section show allowing the user to choose a room to enter                                                                         | Get to the hallway function in each scenario and ensure the ability is there to enter data to choose a room | Each time hallway is called the same results show allowing the user to input their choice of room to go to.                                  | Pass   |
| If 1 is entered does the kitchen function get called                                                                                            | Type 1 into the console to check that the kitchen function loads in the terminal                            | Kitchen functions correctly loads after inputting 1 from the hallway function                                                                | Pass   |
| If 2 is entered does the ballroom function get called                                                                                           | Type 2 into the console to check that the ballroom function loads in the terminal                           | Ballroom function correctly loads after inputting 2 from the hallway function                                                                | Pass   |
| If 3 is entered does the library function get called                                                                                            | Type 3 into the console to check that the library function loads in the terminal                            | Library function correctly loads after inputting 3 from the hallway function                                                                 | Pass   |
| If 4 is entered does the dining hall function get called                                                                                        | Type 4 into the console to check that the dining hall function loads in the terminal                        | Dining Hall function correctly loads after inputting 4 from the hallway function                                                             | Pass   |
| If 5 is entered does the office function get called                                                                                             | Type 5 into the console to check that the office function loads in the terminal                             | Office function correctly loads after inputting 5 from the hallway function                                                                  | Pass   |
| If 6 is entered does the stairs function get called                                                                                             | Type 6 into the console to check that the stairs function loads in the terminal                             | Stairs function correctly loads after inputting 6 from the hallway function                                                                  | Pass   |
| If anything else is entered other than 1 - 6 is the user prompted of incorrect input and asks the options to enter a number between 1 - 6 again | Type a selection of other characters to see if incorrect input shows and input asked again                  | Entering any other character(s) beside 1 - 6 shows incorrect input and question is asked to the user again to enter a number between 1 and 6 | Pass   |



#### kitchen()

| Test                                                                                                                                                                                            | Action                                                                                                                                                             | Expected                                                                                                                                               | Result |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| Go to the kitchen before collecting the item from this room to ensure kitchen_continue is called                                                                                                | Type 1 in the hallway function to call kitchen function. As item has not been collected wait for the kitchen continue function to call and text display correctly. | After typing 1 in the hallway function, kitchen correctly loads and then calls kitchen continue as item is set to False.                               | Pass   |
| Go to the kitchen after already being in the room and collecting the item to ensure the function checks if the global item is true. Notfiying the user of this and calling the hallway function | Visit the kitchen function and collect the item, then enter 1 again in the hallway.                                                                                | Kitchen function prints out that the user already has collected the item from this room and sends them back to the hallway to choose a different door. | Pass   |



#### kitchen_continue()

| Test                                                                                                                                                       | Action                                                                                | Expected                                                                                                                                      | Result |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Does function call after user has entered the kitchen and does not have the item                                                                           | Enter the kitchen for the first time                                                  | User gets kitchen function that goes straight to kitchen continue and displays correctly in the terminal.                                     | Pass   |
| Does input option appear and display correctly                                                                                                             | Wait for text to finish printing and see input option for user to enter their choice. | Input section appears correctly and allows user to input their choice.                                                                        | Pass   |
| If user enters a as option does the hammer correctly append to the backpack and get set as True in global scope. Does the hallway function then get called | Enter the kitchen and type a in the console.                                          | Hammer is appended to backpack and shows in console also setting item to True. User is then taken back to the hallway to choose another room. | Pass   |
| If user enters option b does the game end correctly, calling the play_again function                                                                       | Enter the kitchen and type b in the console                                           | Game over appears, telling the user they have failed the game and then loads play_again function so they can choose to play again or not.     | Pass   |
| If user enters anything else other than 'a' or 'b' the prompt is shown for incorrect input and asks them to input a or b again.                             | Enter the kitchen and type something else other than a or b into the console.        | Message correctly shows that the user has entered something other than a or b and asks the question again.                                  | Pass   |



#### ballroom()

| Test                                                                                                                                                                                             | Action                                                                                                                                                              | Expected                                                                                                                                                | Result |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Go to the ballroom before collecting the item from this room to ensure ballroom_continue is called                                                                                               | Type 2 in the hallway function to call ballroom function. As item has not been collected wait for the ballrom continue function to call and text display correctly. | After typing 1 in the hallway function, ballroom correctly loads and then calls kitchen continue as item is set to False.                               | Pass   |
| Go to the ballroom after already being in the room and collecting the item to ensure the function checks if the global item is true. Notfiying the user of this and calling the hallway function | Visit the ballroom function and collect the item, then enter 2 again in the hallway.                                                                                | Ballroom function prints out that the user already has collected the item from this room and sends them back to the hallway to choose a different door. | Pass   |



#### ballroom_continue()

| Test                                                                                      | Action                                                                                                         | Expected                                                                                                             | Result |
| ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------ |
| Only calls the function if the user has not collected the item from this room and escaped | Type 2 in the hallway function for the first time.                                                             | Calls correctly and displays option to user to choose from                                                           | Pass   |
| Do the input options appear correctly for the user to choose from                         | Wait for ballroom function to finish and check that input option appears, clearing showings options a, b and c. | User can easily type their choice of direction into the console via the input method                                 | Pass   |
| Check option a gets the key, adds to the back pack and escapes room back to hallway       | Type a into the console to choose option a                                                                     | Option a correctly appends key to the backpack and allows user to escape the room. Then calling the hallway function | Pass   |
| Check option b is a dead end and asks directions again                                    | Type b into the console to choose option b                                                                     | Option b correctly goes to a dead end and asks questions again                                                       | Pass   |
| Check option c results in game over                                                       | Type c into the console to choose option c                                                                     | Option c results in game over, calling the play again function                                                       | Pass   |
| If input is not a, b or c, user is prompted about incorrect input and asked options again | Type a different character into the terminal other than a, b or c                                              | If any other character is entered other than a, b or c user is asked to choose again due to incorrect input          | Pass   |



#### library()

| Test                                                                                                                                                                                             | Action                                                                                                                                                             | Expected                                                                                                                                               | Result |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| Go to the library before collecting the item from this room to ensure library_continue is called                                                                                                 | Type 3 in the hallway function to call library function. As item has not been collected wait for the library continue function to call and text display correctly. | After typing 3 in the hallway function, library correctly loads and then calls library continue as item is set to False.                               | Pass   |
| Go to the ballroom after already being in the room and collecting the item to ensure the function checks if the global item is true. Notfiying the user of this and calling the hallway function | Visit the library function and collect the item from the dining hall continue function, then enter 3 again in the hallway to reenter the room.                     | Library function prints out that the user already has collected the item from this room and sends them back to the hallway to choose a different door. | Pass   |



#### library_continue()

| Test                                                                                                                                                        | Action                                                                                                                                                   | Expected                                                                                                                                                                                                                  | Result |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Do 3 options show in the decisions section if the Hammer item has not been collected                                                                        | Ensure Kitchen has not been explored so Hammer is False. Enter library and wait for options to appear                                                    | Only options 1, 2 and 3 are given to the user to choose from.                                                                                                                                                             | Pass   |
| Does option 4 get added to the decisions if the hammer item has been collected                                                                              | Go to the kitchen, choose option a to get the hammer. Visit library and wait for options to appear                                                       | Option 4 is added to the decisions. Giving the user a choice of options 1, 2, 3 and 4                                                                                                                                     | Pass   |
| Do the decision options correctly merge into the input section                                                                                              | Repeat processes above and check that the input section displays correct amount of options based on whether or not the hammer has been collected or not. |                                                                                                                                                                                                                           | Pass   |
| If option 1 is chosen does this call the dining_hall function                                                                                               | Select option 1 by entering '1' into the console                                                                                                         | Correctly displays text and calls the dining hall function                                                                                                                                                                | Pass   |
| If option 2 is chosen does this call the hallway function                                                                                                   | Select option 2 by entering '2' into the console                                                                                                         | Correctly displays text and calls the hallway function                                                                                                                                                                    | Pass   |
| If option 3 is chosen does the game end and call play_again function                                                                                        | Select option 3 by entering '3' into the console                                                                                                         | Correctly displays text and ends in Game over, calling the play_again function                                                                                                                                            | Pass   |
| If the user has the hammer and chooses option 4 does this get the code , then clear the display (clear_display() function) and then go back to the hallway. | Select option 4 by entering '4' into the console                                                                                                         | Correctly shows that the user has guessed the code, and shows the user the code. Due to the gameplay, the user has a few seconds to remember the code and then the clear display function is called clearing the console. | Pass   |
| If any other character is added to the input section, does this flag as incorrect input and ask options correctly again                                     | Enter a number or character that is not 1, 2 or 3 or 4 if hammer is True                                                                                 | Incorrect input is shown and asks user for input again that is correct                                                                                                                                                    | Pass   |



#### dining_hall()

| Test                                                                                                                                                                                                | Action                                                                                                                                                                     | Expected                                                                                                                                                   | Result |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Go to the dining hall before collecting the item from this room to ensure dining_hall_continue is called                                                                                            | Type 4 in the hallway function to call dining hall function. As item has not been collected wait for the dining hall continue function to call and text display correctly. | After typing 4 in the hallway function, dining hall correctly loads and then calls dining hall continue as item is set to False.                           | Pass   |
| Go to the dining hall after already being in the room and collecting the item to ensure the function checks if the global item is true. Notfiying the user of this and calling the hallway function | Visit the dining hall function and collect the item from dining hall continue, then enter 4 again in the hallway.                                                          | Dining hall function prints out that the user already has collected the item from this room and sends them back to the hallway to choose a different door. | Pass   |



#### dining_hall_continue()

| Test                                                                                                                        | Action                                                                                                                                  | Expected                                                                                                | Result |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------ |
| Does the code correctly print out the dictionary values to the terminal                                                     | Enter the room and wait for print statements to load                                                                                    | Values of the dictionary correctly print to the terminal                                                | Pass   |
| Does the code correctly print out the dictionary key to the terminal                                                        | Enter the room and wait for print statements to load                                                                                    | Keys of the dictionary correctly print to the terminal                                                  | Pass   |
| Does the input option appear correctly for the user to interact with                                                        | Wait for input option to appear and type appropriate option into the terminal                                                           | Input correctly appears allowing the user to type their answer.                                         | Pass   |
| Does option a add the blueprints to the back pack correctly                                                                 | Type a into the console to take the items                                                                                               | Mansion details is appended to the backpack and the user leaves the room, calling the hallway function | Pass   |
| Does option b correctly send the user back to the hallway                                                                   | Type b into the console, leaving the items behind                                                                                       | Hallway function is called, no items append to backpack.                                                | Pass   |
| If any other character that is not a and b is entered does the incorrect input text appear and ask the user for input again | Type any other character into the console and wait for incorrect input to show along with the ability to enter an correct option again. | Incorrect input is shown, asking the user the question again and to enter a correct option.             | Pass   |



#### office()

| Test                                                                                                                                              | Action                                                                                                          | Expected                                                                                                                                                                                        | Result |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| Does the first set of options display correctly                                                                                                   | Type 5 in the terminal from the hallway function                                                                | Enters the room and correctly shows the user options a or b to choose from.                                                                                                                     | Pass   |
| If option a is selected is the hallway function called                                                                                            | Type a into the terminal and wait for hallway to be called                                                      | Hallway function correctly loads after option a is selected                                                                                                                                     | Pass   |
| If option b is selected does this then ask the next set of options to the user                                                                    | Type b into the terminal and wait for the next set of options to be provided in the terminal                    | Rest of the function correctly loads after b is selected.                                                                                                                                       | Pass   |
| If anything else is entered in the input section that is not a and b does the incorrect input error show and ask for correct input again          | Type any other character into the terminal that is not 'a' or 'b'.                                              | Incorrect input appears and asks users to enter a correct value.                                                                                                                                | Pass   |
| If the code has not been located do options 1 and 2 show in the input section                                                                     | Go to the office (option 5 from the hallway function) before entering the room where the user locates the code. | Only options 1 and 2 show to the user as Code is still set to False                                                                                                                             | Pass   |
| If the code has been located does option 3 show as well as 1 and 2                                                                                | Go to the kitchen and get the hammer, go to the library and get the code and then enter the office function.    | Options 1, 2 and 3 show to the user as they have collected the code from the library function.                                                                                                  | Pass   |
| If anything else is entered in the second input section that is not a and b does the incorrect input error show and ask for correct input again   | Type any other character into the terminal that is not 1 or 2 if code is False or 3 if code is True.            | Incorrect input appears and asks users to enter a correct value.                                                                                                                                | Pass   |
| If option 1 is chosen does this take the user back to the hallway                                                                                 | Type 1 into the terminal                                                                                        | Hallway function is called correctly                                                                                                                                                            | Pass   |
| If option 2 is chosen does this result in giving the user a one time guess of the code to input. Then show game over and call play_again function | Type 2 into the terminal                                                                                        | Input option appears to guess a code, user can then enter anything they link, but upon clicking enter the game over text shows and calls play_again asking the user if they want to play again. | Pass   |
| If option 3 is chosen when code is true, does this result in giving the user the option to input the correct code.                                | Type 3 into the terminal and wait for input code to appear                                                      | Option to enter the access code appears correctly allowing the user to enter the code the discovered earlier on.                                                                                | Pass   |
| Does entering the correct code result in game win, calling the game_win function                                                                  | Enter correct code into the terminal                                                                            | Game win, prints message to the console, then clears the console and asks if the user wants to play again.                                                                                      | Pass   |
| Does entering the incorrect code ask for the correct code again                                                                                   | Enter an incorrect code into the terminal                                                                       | Asks user to re enter code correctly. Will repeat this until correct code is added.                                                                                                             | Pass   |



#### stairs()

| Test                                                            | Action                                                                    | Expected                                                                                 | Result |
| --------------------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------ |
| Chose option 6 from hallway and ensure stair function is called | Type 6 in the hallway function                                            | Stairs function loads correctly                                                          | Pass   |
| Function results in game over finally calling play_again        | Wait for function to print text, then see the play_again function display | After all text is printed to the terminal. The user is asked if they want to play again. | Pass   |



#### clear_display()

| Test                                                                                  | Action                                                                                                                                                          | Expected                                                                          | Result |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------ |
| Does clear display correctly clear the display when called. Tested on Mac and Windows | Run through game to get to the stages where clear_display is called and check that terminal clears correctly and then continues with the next function or text. | Console correctly clears when called on Macbook Pro and Lenovo Thinkpad (Windows) | Pass   |



### Bugs / Other

Most bugs occurred due to typos in functions and time.sleep typos.

I had an issue with declaring global variables as they were called before. This was due to referencing them more than once in a function based on the way I wanted to set it up. I decided to separate functions with _continue when declaring global variables as 'True' or 'False'.



## Deployment

### GitHub

This project was developed by using the specialized [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) which simulates a terminal in the web browser to play the project. 

1. Click Use this template.
2. Name the repository something appropriate to the project.
3. Copy the repository link into CodeAnywhere to use the template within the IDE.

### Version Control

The site was created using the CodeAnywhere code editor and pushed to github.

The following git commands were used throughout development to push code to the remote repo:

1. git add . - This command was used to add the file(s) to the staging area before they are committed.

2. git commit -m “commit message” - This command was used to commit changes to the local repository queue, ready for the final step.

3. git push - This command was used to push all committed code to the repository on github.


### **Final Deployment with Heroku**

The below steps were followed to deploy this project to the Heroku App:

1. Go to [Heroku](https://dashboard.heroku.com/apps) and click "New" to create a new app.
2. After choosing the app name and setting the region, press "Create app".
3. In "Settings", navigate to Buildpacks and add buildpacks for Python and NodeJS (in order).
4. Leave "Settings" and go to "Deploy". Scroll down and set Deployment Method to GitHub.
Once GitHub is chosen, find your repository by typing in the name and connecting it to Heroku.
5. Scroll down to Manual Deploy, make sure the "main" branch is selected, and click "Deploy Branch". 
6. The deployed app can be found [here]().

## Credits

I used [Geeks for Geeks](https://www.geeksforgeeks.org/clear-screen-python/) for the code in the clear_display function so that the console would be cleared at particular times.

I used [Lucid Chart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucid%20chart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236004&km_CPC_TargetID=kwd-55720648523&km_CPC_Country=1006984&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gad_source=1&gclid=Cj0KCQiAzoeuBhDqARIsAMdH14H3VQDVvCMFaJMPK_U96cnlAH2tstOaQgt56FI7YiNTu4H57idfyRQaAr1gEALw_wcB) to create the flow diagram of the project. This helped with putting the project together and testing the project during and upon completion.

I used [Code Institutes PEP8 Linter](https://pep8ci.herokuapp.com/) to run my python code through to check for any errors.

[Table to Markdown](https://tabletomarkdown.com/) to use tables in ReadME document for testing.

Thanks to Daisy Mc Girr for assisting me through this project and answering questions I had around coding and testing. Also giving me the idea of doing an adventure based text game.

The Code Institute lessons and Love Sandwiches walkthrough for knowledge on coding Python.

