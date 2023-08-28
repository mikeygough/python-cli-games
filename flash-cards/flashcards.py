# import the json module from python3
import json

# open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)
    # debug
    # print(data)
# note, the only difference between JSON and a python dictionary is the keys have '' 
# single quotes whereas the JSON has "" double-quotes.

# initialize total as the length of the cards array
total = len(data["cards"])
# initialize score as 0
score = 0

for i in data["cards"]:
    guess = input(i["q"] + " > ")

    if guess.lower() == i["a"].lower():
        # increment score up one
        score += 1
        # interpolate score and total into the response
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")

print(f"\nThanks for studying! \nFinal Score {score}/{total}")