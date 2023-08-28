# Import the random method from the randint module
from random import randint

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0,2)]

player = False

while player == False:
    # Get player input
    player = input("Bear, Ninja, or Cowboy? > ")

    # Compare computer and player role

    if computer == player:
      print("DRAW!")
    elif computer == "Cowboy":
      if player == "Bear":
        print("You lose!", computer, "shoots", player)
      else: # computer is cowboy, player is ninja
        print("You win!", player, "defeats", computer)
    elif computer == "Bear":
      if player == "Cowboy":
        print("You win!", player, "shoots", computer)
      else: # computer is bear, player is ninja
        print("You lose!", computer, "eats", player)
    elif computer == "Ninja":
      if player == "Cowboy":
        print("You lose!", computer, "defeats", player)
      else: # computer is ninja, player is bear
        print("You win!", player, "eats", computer)

    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      player = False
      computer = roles[randint(0,2)]
    else:
      break

''' Stretch Goals
Currently inputting a not recognized name (like Anteater) wins two out of three times. You can solve this with a couple approaches. Test the input string and display a message if the name is not allowed for example: Ant is not Bear, Cowboy, or Ninja or Bear, Cowboy, and Ninja are the only allowed names.

Start the game with a get ready message! "Get ready to play Bear, Ninja, Cowboy!"

Follow the start message with an option to get instructions. "Would you like instructions? (yes/no) >" If yes show some instructions, something like: "Bear, Ninja, Cowboy is an exciting game of strategy and skill! Pit your wit against the computer! Choose a player: Bear, Ninja, or Cowboy. The computer chooses a player. Bear eats Ninja, Ninja defeats Cowboy and cowboy shoots bear."

Comment your code! Pay close attention to the formatting and code blocks.

Break your code into functions! Use functions to handle specific operations. Using functions is an important and coding best practice!

Keep score. Add 1 for each game you win subtract 1 for each game lost. Show the score after each game.

  Expand the game. Look up Rock, Paper, Scissors, Lizard, Spock. This is the same game but has five possible plays. Rock < Paper < Scissors < Lizard < Spock < Rock
'''