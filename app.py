import random

state_capitals = [
  {
    "name": "Alabama",
    "capital": "Montgomery"
  },
  {
    "name": "Alaska",
    "capital": "Juneau"
  },
  {
    "name": "Arizona",
    "capital": "Phoenix"
  },
  {
    "name": "Arkansas",
    "capital": "Little Rock"
  },
  {
    "name": "California",
    "capital": "Sacramento"
  },
  {
    "name": "Colorado",
    "capital": "Denver"
  },
  {
    "name": "Connecticut",
    "capital": "Hartford"
  },
  {
    "name": "Delaware",
    "capital": "Dover"
  },
  {
    "name": "Florida",
    "capital": "Tallahassee"
  },
  {
    "name": "Georgia",
    "capital": "Atlanta"
  },
  {
    "name": "Hawaii",
    "capital": "Honolulu"
  },
  {
    "name": "Idaho",
    "capital": "Boise"
  },
  {
    "name": "Illinois",
    "capital": "Springfield"
  },
  {
    "name": "Indiana",
    "capital": "Indianapolis"
  },
  {
    "name": "Iowa",
    "capital": "Des Moines"
  },
  {
    "name": "Kansas",
    "capital": "Topeka"
  },
  {
    "name": "Kentucky",
    "capital": "Frankfort"
  },
  {
    "name": "Louisiana",
    "capital": "Baton Rouge"
  },
  {
    "name": "Maine",
    "capital": "Augusta"
  },
  {
    "name": "Maryland",
    "capital": "Annapolis"
  },
  {
    "name": "Massachusetts",
    "capital": "Boston"
  },
  {
    "name": "Michigan",
    "capital": "Lansing"
  },
  {
    "name": "Minnesota",
    "capital": "St. Paul"
  },
  {
    "name": "Mississippi",
    "capital": "Jackson"
  },
  {
    "name": "Missouri",
    "capital": "Jefferson City"
  },
  {
    "name": "Montana",
    "capital": "Helena"
  },
  {
    "name": "Nebraska",
    "capital": "Lincoln"
  },
  {
    "name": "Nevada",
    "capital": "Carson City"
  },
  {
    "name": "New Hampshire",
    "capital": "Concord"
  },
  {
    "name": "New Jersey",
    "capital": "Trenton"
  },
  {
    "name": "New Mexico",
    "capital": "Santa Fe"
  },
  {
    "name": "New York",
    "capital": "Albany"
  },
  {
    "name": "North Carolina",
    "capital": "Raleigh"
  },
  {
    "name": "North Dakota",
    "capital": "Bismarck"
  },
  {
    "name": "Ohio",
    "capital": "Columbus"
  },
  {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
  },
  {
    "name": "Oregon",
    "capital": "Salem"
  },
  {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
  },
  {
    "name": "Rhode Island",
    "capital": "Providence"
  },
  {
    "name": "South Carolina",
    "capital": "Columbia"
  },
  {
    "name": "South Dakota",
    "capital": "Pierre"
  },
  {
    "name": "Tennessee",
    "capital": "Nashville"
  },
  {
    "name": "Texas",
    "capital": "Austin"
  },
  {
    "name": "Utah",
    "capital": "Salt Lake City"
  },
  {
    "name": "Vermont",
    "capital": "Montpelier"
  },
  {
    "name": "Virginia",
    "capital": "Richmond"
  },
  {
    "name": "Washington",
    "capital": "Olympia"
  },
  {
    "name": "West Virginia",
    "capital": "Charleston"
  },
  {
    "name": "Wisconsin",
    "capital": "Madison"
  },
  {
    "name": "Wyoming",
    "capital": "Cheyenne"
  }
]

correct = 0
wrong = 0
guesses = 0

print('Learn all the US Capitals!!')
start_question = input('Ready to begin? [y/n] ').lower()

while guesses < 51:

    if guesses == 50:
        end_message = input(f'GAME OVER, you have gone through all the states. Your final score was {correct} correct, and {wrong} incorrect. Would you like to play again? [y/n]' ).lower()

        if end_message == 'y':
            correct = 0
            incorrect = 0
            tries = 0
        else:
            print('See ya later!')

    if start_question == 'y':
        random.shuffle(state_capitals)
        for state in state_capitals:
            question = input(f'What is the state capital of {state["name"]}? ').title()
            if question == state["capital"]:
                print(f'Correct! You guessed {question}')
                guesses += 1
                correct += 1
                print(f'You have correctly guessed {correct} state/s')
                print(f'You have incorrectly guessed {wrong} state/s')
                print(f'{guesses} total guesses')

            else: 
                print(f'Sadly, {question} is incorrect. Try again!')
                wrong += 1
                guesses += 1
                print(f'You have correctly guessed {correct} state/s')
                print(f'You have incorrectly guessed {wrong} state/s')
                print(f'{guesses} total guesses')

    else:
        print('You are missing out') 