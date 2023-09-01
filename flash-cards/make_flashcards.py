# companion file to flashcards.py... this program allows users to make flashcards!
# imports
import json
import os


def write_file(file_name, data):
    ''' write_file() writes the given data (dictionary) to the specified .json file. '''
    
    with open(file_name, 'w') as f:
        # indent for pretty formatting
        json.dump(data, f, indent=2)


def get_deck_data():
    ''' get_deck_data() initializes a dictionary to store deck information. it then
    prompts the user for a deck title and card information. after adding each card
    the user can decide to add another card or exit the process and save the deck. '''

    
    print("Collecting data for new deck...")
    # initialize new deck dictionary
    new_deck = {"title": None, "cards": []}
    
    # get deck title
    new_deck_title = input("What do you want to name the deck? ")
    # set deck title
    new_deck["title"] = new_deck_title
    
    # get card data
    inputting = True
    while inputting:
        
        # get question (front of card) and answer (back of card)
        question = input("Front of card: ")
        answer = input("Back of card: ")
        
        # create card
        card = {"q": question, "a": answer}
        
        # add to deck
        new_deck["cards"].append(card)
        
        # check for more cards
        if input("Still adding? (y/n) ") == 'n':
            break
        
    return new_deck

# main    
print("Welcome to the flashcard factory!\n")

new_deck = get_deck_data()

# set file_name
file_name = new_deck["title"].lower().replace(' ', '-')

# save deck
write_file(f"decks/{file_name}.json", new_deck)

print(f"{new_deck['title']} deck successfully saved!")