# Program Outline:

We have basically six steps:

1. Setup the cards data that we want to quiz ourselves with
2. Write code that reads the cards data and parses it into a python dictionary
3. Write code that iterates over the cards
4. Get the users's input for each question
5. Check the users input against the answer
6. Display "Correct!" or "Incorrect!"

Supports the following features:
[X] Ask them if they want to study again at the end.
[X] Randomize the order of questions.
[X] Keep playing until the player gets all the questions right at least once.
[X] Create various data files that are different sets of questions and let users pick which one they want to do. Users can select based on key instead of deck title.
[X] Let users enter their own cards and save those as libraries of questions and answers. -> in make_flashcards.py.
[X] Adding a title to a deck (more human readable form of the filename).

#### Write pseudo code that describes the flashcards game.

FUNCTION read_file:
  INPUTS file_name
  
  INITIALIZE data
  SET data = READ file_name as json
  DISPLAY "Successfully loaded" + file_name
  RETURN  data
END FUNCTION


FUNCTION get_decks:
  INITIALIZE decks_list
  
  FOR file in decks directory:
    add deck to decks_list, remove '.json' portion of string
  END FOR

  INITIALIZE decks_dict
  FOR count, value in enumerate(decks_list)
    SET decks_dict[count] = value
  END FOR
  
  RETURN decks_list
END FUNCTION


FUNCTION select_deck:
  INPUTS available_decks
  
  DISPLAY "Available Decks"
  FOR deck in available_decks:
    DISPLAY deck_key + deck_value
  END FOR

  GET deck_choice, PROMPT "Please choose a deck to study: "

  START WHILE LOOP, while deck_choice not in available_decks:
    DISPLAY "Invalid deck! Please try again."
    GET deck_choice, PROMPT "Please choose a deck to study: "
  END WHILE LOOP

  RETURN available_decks["deck_choice"]
END FUNCTION


FUNCTION study_deck:
  INPUTS deck

  INITIALIZE total
  SET total = length cards in deck

  INITIALIZE score
  SET score = 0

  FOR card in deck["cards"]:
    DISPLAY card
    GET guess, PROMPT card + "> "
    IF guess.lower() == card["answer"].lower():
      SET score = score + 1
      DISPLAY "Correct! Current score: " + score / total
    ELSE
      DISPLAY "Incorrect! The correct answer was: " + card["answer"]
      DISPLAY "Current score: " + score / total
    END IF
  END FOR
  DISPLAY "Final score: " + score / total
  RETURN score, total
END FUNCTION


INITIALIZE decks
SET decks = get_decks()

INITIALIZE deck_choice
SET deck_choice = select_deck(available_decks=decks)

INITIALIZE data
SET data = read_file(file_name=deck_choice + ".json")

INITIALIZE study
SET study = True

START WHILE loop, while study == True:

  shuffle data["cards"]

  INITIALIZE score, INITIALIZE total
  SET score, total = study_deck(deck=data)

  IF score not equal to total:
    IF score / total <= 0.5:
      DISPLAY "You need practice..."
    ELSE IF score / total > 0.5:
      DISPLAY "Good work..."
    END IF
    DISPLAY "Looks like you haven't mastered the material yet... Let's review again!"
  ELSE:
    DISPLAY "Amazing... You scored 100%!"
    INITIALIZE study_again
    GET study_again, PROMPT "Would you like to study again? (yes/no) > "
    IF study_again == "yes":
      SET study = True
    ELSE:
      BREAK
    END IF
  END IF
END WHILE LOOP