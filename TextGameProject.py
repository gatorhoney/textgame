
# 'Save the Everglades' environmental theme text game
# Amanda Coleman 2022
# test comment



import os

#Welcome to game message and explanation of game rules and moves
def prompt():
    print("\t\t\t Welcome to the Everglades!\n\n"
          "You must collect all 6 pieces of the Carved Gator Idol to defeat the Developers and save the swamp.\n\n"
          "Moves: \t 'go {direction}' (travel north, south, east, or west)\n"
          "\t 'get {item}' (add nearby item to inventory)\n\n")
    input("Press any key to continue ... ")


#clears screen

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(prompt())

print(clear())

#Map


rooms = {
    'Gator Nest': {'East': 'Coastal Mangroves'},
    'Coastal Mangroves': {'West':'Gator Nest', 'South': 'Brackish Salt Flats', 'East': 'Hardwood Hammocks', 'Item': 'Carved Gator Jaw Bone'},
    'Brackish Salt Flats': {'North': 'Coastal Mangroves', 'East': 'Wet Prairie', 'Item': 'Carved Gator Jaw Bone 2'},
    'Wet Prairie': {'West': 'Brackish Salt Flats', 'East': 'Cypress Grove', 'North': 'Hardwood Hammocks', 'Item': 'Carved Gator Torso'},
    'Hardwood Hammocks': {'South': 'Wet Prairie', 'East': 'Freshwater Slough', 'West': 'Coastal Mangroves', 'Item': 'Carved Gator Tail'},
    'Freshwater Slough': {'West': 'Hardwood Hammocks', 'South': 'Cypress Grove', 'Item': 'Left Gator Paw'},
    'Cypress Grove': {'North': 'Freshwater Slough', 'South': 'Cleared and Filled Wetlands', 'Item': 'Right Gator Paw'},
    'Cleared and Filled Wetlands': {'North': 'Cypress Grove', 'Boss': 'Evil Developers'}}


# list to track inventory
inventory = []

# tracks current room
current_room = 'Gator Nest'

# result of last move
msg = ""

clear()


# gameplay loop
while True:

    clear()

    print(f"You are in the {current_room}\n Inventory: {inventory}. \n {'*' * 27}")


    # display message
    print(msg)

    # item indicator
    if "Item" in rooms[current_room].keys():

        nearby_item = rooms[current_room]["Item"]

        # print if item plural
        if nearby_item not in inventory:
                print(f'You see a {nearby_item}')


        # Boss encounter

    if "Boss" in rooms[current_room].keys():

        # You lose!
        if len(inventory) < 6:
            print(f'You failed to collect the items! You lost a fight to {rooms[current_room]["Boss"]}')

        # Win
        else:
            print(f'The pieces of the carved Gator Idol are tinkling together in your satchel. '
                  f'As you near the cleared and filled wetlands, the pieces start to hum and glow. '
                  f'You carefully take them out, hoding them in front of you, bathed in their greenish glow.'
                  f'Ahead of you, the Evil Land Developers rise from the mud with their machines of death ...'
                  f''
                  f'The carved Gator Idol lifts from your hands, shaking and glowing brighter and brighter!'
                  f'In a flash, the Gator Idol turns into a towering Gator God Beast, and in one bite, swallows the Evil Land Developers and their machines whole!'
                  f'With another blinding flash, the Gator God Beast transforms again into 6 fragments of green stone carvings, lying in the mud.'
                  f'You beat {rooms[current_room]["Boss"]}!')
            break

    # accept a player's move as input
    user_input = input('Enter your move:\n')

    # splits move into separate words
    next_move = user_input.split(' ')

    # first word is action
    action = next_move[0].title()

    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = ' '.join(item).title()

        # moving between rooms
        if action == "Go":

            try:
                current_room = rooms[current_room][direction]
                msg = f'You travel {direction}.'

            except:
                msg = f"You can't go that way"


        # picking up items to add to inventory
        elif action == "Get":

            try:

                if item == rooms[current_room]["Item"]:
                    if item not in inventory:
                        inventory.append(rooms[current_room]["Item"])
                        msg = f"{item} retrieved!"

                    else:
                        msg = f"You already have the {item}."
                else:
                    msg = f"Can't find {item}."
            except:
                msg = f"Can't find {item}."


        elif action == "Exit":

            print('Goodbye!')
            break

        # renders other commands invalid
        else:
            print('Enter a valid command!')









