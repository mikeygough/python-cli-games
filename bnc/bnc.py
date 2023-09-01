# Import the random method from the randint module
from random import randint

# get ready message
print("Get ready to play Bear, Ninja, Cowboy!")

# define instructions
instructions = '''Bear, Ninja, Cowboy is an exciting game of strategy and skill! 
Pit your wit against the computer! Choose a player: Bear, Ninja, or Cowboy. The computer chooses a player. 
Bear eats Ninja, Ninja defeats Cowboy and cowboy shoots bear. '''

# would you like instructions?
if input("Would you like instructions? (yes/no) > ").lower() == "yes":
    print(instructions)

# Define roles
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random role using an array
computer = roles[randint(0, len(roles)-1)]

print("Let's begin!")
player = False
# initialize score
score = {"w": 0,
         "l": 0,
         "d": 0}

while player == False:
    # Get player input
    player = input("Bear, Ninja, or Cowboy? > ")

    # ensure valid selection
    while player not in roles:
        print("Invalid role! Please try again.")
        player = input("Please choose a role: Bear, Ninja, or Cowboy? > ")

    # Compare computer and player role
    if computer == player:
      print("DRAW!")
      score["d"] += 1
    elif computer == "Cowboy":
      if player == "Bear":
        print("You lose!", computer, "shoots", player)
        score["l"] += 1
      else: # computer is cowboy, player is ninja
        print("You win!", player, "defeats", computer)
        score["w"] += 1
    elif computer == "Bear":
      if player == "Cowboy":
        print("You win!", player, "shoots", computer)
        score["w"] += 1
      else: # computer is bear, player is ninja
        print("You lose!", computer, "eats", player)
        score["l"] += 1
    elif computer == "Ninja":
      if player == "Cowboy":
        print("You lose!", computer, "defeats", player)
        score["l"] += 1
      else: # computer is ninja, player is bear
        print("You win!", player, "eats", computer)
        score["w"] += 1

    print(f"Current Score: {score['w']} Win(s), {score['l']} Loss(es), {score['d']} Draw(s)!")
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
      player = False
      computer = roles[randint(0,2)]
    else:
      break

print("Thanks for playing!")
print(f"Final Score: {score['w']} Win(s), {score['l']} Loss(es), {score['d']} Draw(s)!")

''' Stretch Goals
[X] Currently inputting a not recognized name (like Anteater) wins two out of three times. 
    You can solve this with a couple approaches. Test the input string and display a message if the 
    name is not allowed for example: Ant is not Bear, Cowboy, or Ninja or Bear, Cowboy, and Ninja are the only allowed names.
[X] Start the game with a get ready message! "Get ready to play Bear, Ninja, Cowboy!"
[X] Follow the start message with an option to get instructions. "Would you like instructions? (yes/no) >" 
    If yes show some instructions, something like: "Bear, Ninja, Cowboy is an exciting game of strategy and skill! 
    Pit your wit against the computer! Choose a player: Bear, Ninja, or Cowboy. The computer chooses a player. 
    Bear eats Ninja, Ninja defeats Cowboy and cowboy shoots bear."
[X] Comment your code! Pay close attention to the formatting and code blocks.
[X] Keep score. Add 1 for each game you win subtract 1 for each game lost. Show the score after each game.

Break your code into functions! Use functions to handle specific operations. Using functions is an important and coding best practice!
Expand the game. Look up Rock, Paper, Scissors, Lizard, Spock. This is the same game but has five possible plays. Rock < Paper < Scissors < Lizard < Spock < Rock
'''