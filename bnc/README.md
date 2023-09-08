# Program Outline:

We have basically four steps:

1. Command Line user input
2. The computer randomly picking a role
3. Checking the player's role and the computer's role
4. Displaying who won

Supports the following features:
[X] Input validation, the user must input a valid role.
[X] Start the game with a get ready message! "Get ready to play Bear, Ninja, Cowboy!"
[X] Users can choose to read the instructions or not.
[X] Score keeping and display after each round plus a final score at the end.

#### Write pseudo code that describes the game Bear, Ninja Cowboy.

DISPLAY "Get ready to play Bear, Ninja, Cowboy!"

INITIALIZE instructions
SET instructions = Game Instructions String

GET instruction_response, PROMPT "Would you like instructions? (yes/no) > "
IF instruction_response.lower() == "yes":
  DISPLAY instructions

INITIALIZE list_of_roles
SET list_of_roles = ["Bear", "Ninja", "Cowboy"]

INITIALIZE computer_role
INITIALIZE random_number
SET random_number = COMPUTE random number between 0 and (length of roles list - 1)
SET computer_role = value of list_of_roles at index position of random_number

DISPLAY "Let's begin!"

INITIALIZE player boolean
SET player = False

INITIALIZE score dictionary with keys win, loss, draw
SET score win, loss and draw values to 0

START WHILE loop, while player == False:
  GET player, PROMPT "Bear, Ninja, or Cowboy? > "

  START WHILE LOOP, while player not in list_of_roles:
    DISPLAY "Invalid role! Please try again."
    GET player, PROMPT "Please choose a role: Bear, Ninja, or Cowboy? > "
  END WHILE LOOP

  IF computer_role == player:
    DISPLAY "DRAW!"
    UPDATE score, add 1 to draw
  ELSE IF computer_role == "Cowboy":
    IF player == "Bear":
      DISPLAY "You lose! + computer_role + "shoots" + player
      UPDATE score, add 1 to loss
    ELSE IF player == "Ninja":
      DISPLAY "You win!" + player "defeats" computer_role
      UPDATE score, add 1 to win
    END IF
  ELSE IF computer_role == "Bear":
    IF player == "Cowboy":
      DISPLAY "You win!" + player "shoots" + computer_role
      UPDATE score, add 1 to win
    ELSE IF player == "Ninja":
      DISPLAY "You lose!" + computer_role + "eats" + player
      UPDATE score, add 1 to loss
    END IF
  ELSE IF computer_role == "Ninja":
    IF player == "Cowboy":
      DISPLAY "You lose!" + computer_role + "defeats" + player
      UPDATE score, add 1 to loss
    ELSE IF player == "Bear":
      DISPLAY "You win!" + player + "eats" + computer_role
      UPDATE score, add 1 to win
    END IF
  END IF

  DISPLAY "Current Score: " + score['wins'] + score['losses'] + score['draws']
  INITIALIZE play_again
  GET play_again, PROMPT "Would you like to play again? (yes/no) > "

  IF play_again == "Yes":
    SET player == false
    SET random_number = COMPUTE random number between 0 and (length of roles list - 1)
    SET computer_role = value of list_of_roles at index position of random number
  ELSE:
    Break
  END IF
END WHILE LOOP

DISPLAY "Thanks for playing!"
DISPLAY "Final Score: " + score['wins'] + score['losses'] + score['draws']