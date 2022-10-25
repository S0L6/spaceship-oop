# main.py

# from room import Room
# from character import Character, Friend, Enemy
# from item import Item

# create rooms
cavern = Room("Cavern")
cavern.description = "A room so big that the light of your torch doesn't reach the walls."

armoury = Room("Armoury")
armoury.description = "The walls are lined with racks that once held weapons and armour!"

lab = Room("lab")
lab.description = "A strange odour hangs in a room filled with unknowable contraptions."

throne_room = Room("Throne Room")
throne_room.description = "Two lava falls light up the room with a throne quadruple the height of you."


cavern.link_rooms(armoury, "south")
armoury.link_rooms(cavern, "north")
armoury.link_rooms(lab, "east")
armoury.link_rooms(throne_room, 'south')
lab.link_rooms(armoury, "west")
throne_room.link_rooms(armoury, "north")

# Create chracters
ugine = Enemy('Ugine')
ugine.description = 'a huge troll with rotting teeth'
ugine.weakness = "cheese"

nigel = Friend('Nigel')
nigel.description = "a burly dwarf with golden beads woven through his beard"
nigel.conversation = "Well youngan, what are you doing here?"

skeleton_king = Enemy('The Skelton King')
skeleton_king.description = 'he looms over you with red glowing eyes!'
skeleton_king.conversation = 'Run before I change my mind about you!'
skeleton_king.weakness = "lava sword"

# add character to rooms
armoury.character = ugine
lab.character = nigel
throne_room.character = skeleton_king

# create items
cheese = Item("Cheese")
cheese.description = "super smelly"

chair = Item("Chair")
chair.description = "designed to be sat on"

elmo = Item("Elmo")
elmo.description = "wanting to be tickled"

lava_sword = Item("lava sword")
lava_sword.description = "a blade that melts through anything"

# add items to room
cavern.item = chair
armoury.item = elmo
lab.item = cheese
throne_room.item = lava_sword

#Init variables
current_room = cavern
running  = True
backpack = []

# ----- MAIN LOOP ----- #
while running:
    current_room.describe()

    command = input("You: > ").lower()
# move
    if command in ["north",'south','east','west']:
        current_room = current_room.move(command)
# talk
    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("There is none here to talk to.")
# hug
    elif command == "hug":
        if current_room.character is not None:
            current_room.character.hug()
        else:
            print("There is no one here to hug.")
# fight   
    elif command == "fight":
        if current_room.character is not None:
            weapon = input("What will you fight with? > ").lower()
            available_weapons = []
            for item in backpack:
                available_weapons.append(item.name)
            if weapon in available_weapons:
                if current_room.character.fight(weapon):
                    current_room.character = None
                    if Enemy.get_num_of_ennemy() == 0:
                        print("You have slain all the enemies your are victorious!")
                        running = False
                else:
                    running = False
            else:
                print(f"You don't have {weapon}.")
                print(f"{current_room.character.name} strikes you down.")
                running = False
        else:
           print("There is no one to fight.")
# take
    elif command == "take":
        if current_room.item is not None:
            backpack.append(current_room.item)
            print(f"You put {current_room.item.name} into your backpack.")
            current_room.item = None
        else:
            print("There is nothing in the room to take.")
# backpack
    elif command == "backpack":
        if backpack == []:
            print("It is empty")
        else:
            print("You have:")
            for item in backpack:
                print(f"- {item.name.capitalize()}")
# help
    elif command == 'help':
        print("Type which direction you wish to move(north, south, east, west),")
        print("or use one of these commands:")
        print("- Talk")
        print("- Fight")
        print("- Hug")
        print("- Take")
        print("- Backpack")
        print("- Quit")

    elif command == 'quit':
        running = False
    else:
        print("Enter 'help' for list of commands")

    input("\nPress <Enter> to continue")

print("Thank you for playing Deepest Dungeon")