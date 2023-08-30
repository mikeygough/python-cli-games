# imports
import json # to read json
import random # to shuffle
import os # to list available decks


def read_file(file_name):
    ''' read_file() opens file_name, a .json file, reads as json
        and returns that data as a dictionary to make flashcards. '''
    with open(file_name, 'r') as f:
        # debug
        # print(data)
        data = json.load(f)
        return data
    

def list_decks():
    ''' list_decks() returns a list of strings with the available decks in ./decks '''
    decks = []
    for deck in os.listdir('./decks'):
        decks.append(deck[:-5])
    return decks


def select_deck(available_decks):
    ''' select_deck() shows the user the available decks and prompts them to select one for study '''
    # display available decks to user
    print("Available Decks:")
    for deck in available_decks:
        print(deck)

    # get deck from user
    deck_choice = input("Please choose a deck to study: ")

    # ensure deck exists
    while deck_choice not in available_decks:
        print("Invalid Deck! Please try again.")
        deck_choice = input("Please choose a deck to study: ")
        
    return deck_choice
  

def play_game(deck):
    ''' play_game() runs through a round of flashcard reviews.
    takes one argument, deck, which is the deck dictionary
    returned from loading data with the read_file() function. '''
   
    # initialize total as the length of the cards array
    total = len(deck["cards"])  
   
     # initialize score as 0
    score = 0
    for i in deck["cards"]:
        guess = input(i["q"] + " > ")
        if guess.lower() == i["a"].lower():
            # increment score up one
            score += 1
            # interpolate score and total into the response
            print(f"Correct! Current score: {score}/{total}")
        else:
            print(f"Incorrect! The correct answer was {i['a']}")
            print(f"Current score: {score}/{total}")
    print(f"\nFinal Score {score}/{total}")
    
    return score, total

# main

# get list of available decks
decks = list_decks()

deck_choice = select_deck(available_decks=decks)

# load data for deck
data = read_file(file_name=f"decks/{deck_choice}.json")

# start study loop
player = True
while player == True:
   
  # shuffle deck
    random.shuffle(data["cards"])
   
    # play game
    score, total = play_game(deck=data)
    
    # didn't pass
    if score != total:
        if score / total <= 0.5:
            print("You need practice...")
        elif score / total > 0.5:
            print("Good work...")
        
        print("Looks like you haven't yet mastered the material... Let's play again!\n")
        play_again = True
    # passed
    else:
        # get user input to continue or break
        print("Amazing... You scored 100%!")
        play_again = input("Would you like to play again? (yes/no) > ")
    
        if play_again == 'yes':
            player = True
        else:
            break

''' Brainstorming New Features
[X] Ask them if they want to play again at the end.
[X] Randomize the order of questions.
[X] Keep playing until the player gets all the questions right at least once.
[X] Create various data files that are different sets of questions and let people pick which one they want to do.
[] Let people enter their own cards and save those as libraries of questions and answers.
[] Keep playing until the player answers correctly 10 in a row.

f-strings - Can you use f-strings to change how we do string interpolations throughout this program?

End game message - print a message when the game ends, something like: "Thanks for playing! You scored: 4 out five correct!"
  To find the number of questions len() to count the cards array.
  Modify the message based on the score:
    Less than half correct: "You need practice..."
    More than half correct: "Good work..."
    All correct: "Amazing..."

Use functions to organize your code.
  Use a function to read the data file.
    This function might take the file path as a parameter
    And return the data that was loaded
  Use a function to display the next question
    This function might take the question and the answer as a parameter
    And return True or False if the question was answered correctly
  Write a function to display game messages
    You might have a function to display a starting message
    You might have a quwstion to display an end game message
'''