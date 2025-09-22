#importing random module
import random

Catagory =input("Choose a category (sports/politics): ").strip().lower()

#lists of subjects, actions, and places/things
subjects_sports= ["Sakib Al Hasan", 
          "Mashrafe Bin Mortaza", 
          "Tamim Iqbal", 
          "AB de Villiers",
            "Chris Gayle",
            "Virat Kohli",
            "Mushfiqur Rahim",
            "Misel Marsh",
            "David Warner"
        ]
subjects_politics= ["Prime Minister",
          "President",
          "Opposition Leader",
          "Foreign Minister",
          "Finance Minister",
          "Health Minister",
          "Education Minister",
          "Defense Minister",
          "Home Minister"
        ]
actions_sports= ["speaking", 
          "driving", 
          "orders", 
          "crying", 
          "celebrates", 
          "waiting", 
          "sleeping", 
          "drinking", 
          "dancing"
        ]
actions_politics= ["announcing",
          "signing",
          "meeting",
          "debating",
          "campaigning",
          "visiting",
          "addressing",
          "negotiating",
          "protesting"
        ]

places_or_things= ["During ICC T20 World Cup 2024", 
          "at Lal Dighi", 
          "at Elevated Expressway ", 
          "at Neval", 
          "Maowa", 
          "Fruit Beer", 
          "Runway", 
          "at Airport", 
          "at Duty Free Shop"
        ]

#headlines generator loop
while True:
    if Catagory=="sports":
        subjects=subjects_sports
        actions=actions_sports
    elif Catagory=="politics":
        subjects=subjects_politics
        actions=actions_politics

    subject = random.choice(subjects)
    action = random.choice(actions)

    Recom = input("Any recomandation for place (yes/no): ").strip().lower()
    if Recom=="yes":
        places_or_things.append(input("Enter your recomandation: ").strip())
        place_or_thing = places_or_things[-1]  # Get the last added recommendation
    else: 
        place_or_thing = random.choice(places_or_things)

    headline = f" Breaking News: {subject} {action} {place_or_thing}"
    print("\n"+headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input != 'yes':
        break

#Popup message
print("Thank you for using the headline generator!")

