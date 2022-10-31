##### MAIN #####

# Modules
from character import Character, Friend, Enemy
from room import Room
import random, time, os

# Create Rooms for Spaceship
bridge = Room('Bridge')
bridge.description = 'Once was the main control room of the spaceship with large vines growing through the control panels.'

gym = Room('Gym')
gym.description = 'A big open space with windows outlooking the lush planet. Gym equipment line the walls and floors.'

crew_quaters = Room('Crew Quaters')
crew_quaters.description = 'Once housed the crew of the ship. Empty messy beds line the walls. Multiple Cryogenic chambers sit next to the beds with your dead crewmates inside.'

defense_room = Room('Defense Room')
defense_room.description = 'Defense systems for detectig and destroying asteroids using exterior guns sit in the middle of the small cramped room.'

bar = Room('Bar')
bar.description = 'Hard liqour sit on shelves behind the bar with dimly lit candles lighting up the room.'

life_support = Room('Life Support')
life_support.description = 'Life support systems not functioning properly warning lights illuminating the room. Could be the cause of abandonment?'

server_room = Room('Server Room')
server_room.description = 'Racks of servers are stacked to the ceiling looking lifeless with no blinking lights.'

armoury = Room('Armoury')
armoury.description = 'Guns line the walls'

cargo_hold = Room('Cargo Hold')
cargo_hold.description = 'The main storage in the ship. You could probably find some valuable things in'

eco_cont = Room('Ecosystem Containment')
eco_cont.description = 'Plants cover all surfaces in the open room. Overgrown vines flow through the doors to the rest of the ship.'

nuclear_reactor = Room('Nuclear Reactor')
nuclear_reactor.description = 'Green liquid seeps from the large glass silo. Defening sirens blaring warning signals due to a radioactive leak.'

power = Room('Power')
power.description = 'All the power runs through this room into the engines.'

solar_array = Room('Solar Array')
solar_array.description = 'Broken Solar panels line the walls. Perhaps they were meant to replace the ones on the outside.'

lengine_room = Room('Left Engine Room')
lengine_room.description = 'An open room with acccess to the ion engines for repairs.'

maintenance = Room('Maintanence Storage')
maintenance.description = 'A room with tools and maintenance equipment for the engineers.'

air_lock = Room('Air Lock')
air_lock.description = 'An airlock for accessing the outside of the ship.'

rengine_room = Room('Right Engine Room')
rengine_room.description = 'An open room with acccess to the ion engines for repairs.'

# Linking Rooms together
bridge.link_rooms(crew_quaters, "south")

gym.link_rooms(crew_quaters, "west")
gym.link_rooms(bar, "south")

crew_quaters.link_rooms(bridge, "north")
crew_quaters.link_rooms(defense_room, "east")
crew_quaters.link_rooms(life_support, "south")
crew_quaters.link_rooms(gym, "west")

defense_room.link_rooms(crew_quaters, "west")
defense_room.link_rooms(server_room, "south")

bar.link_rooms(gym, "north")
bar.link_rooms(life_support, "east")
bar.link_rooms(armoury, "south")

life_support.link_rooms(crew_quaters, "north")
life_support.link_rooms(server_room, "east")
life_support.link_rooms(cargo_hold, "south")
life_support.link_rooms(bar, "west")

server_room.link_rooms(defense_room, "north")
server_room.link_rooms(life_support, "west")
server_room.link_rooms(eco_cont, "south")

armoury.link_rooms(bar, "north")
armoury.link_rooms(cargo_hold, "west")

cargo_hold.link_rooms(life_support, "north")
cargo_hold.link_rooms(eco_cont, "west")
cargo_hold.link_rooms(power, "south")
cargo_hold.link_rooms(armoury, "east")

nuclear_reactor.link_rooms(power, "west")

power.link_rooms(cargo_hold, "north")
power.link_rooms(solar_array, "west")
power.link_rooms(maintenance, "south")
power.link_rooms(nuclear_reactor, "east")

solar_array.link_rooms(power, "east")

lengine_room.link_rooms(maintenance, "east")

maintenance.link_rooms(power, "north")
maintenance.link_rooms(rengine_room, "east")
maintenance.link_rooms(air_lock, "south")
maintenance.link_rooms(lengine_room, "west")

rengine_room.link_rooms(maintenance, "west")

# Create CHaracters
bob = Friend('Bob The Bartender')
bob.description = 'A friendly robotic bartender that serves alchohol.'
bob.conversation = ['What brings you onboard?', 'This ship is in critical condition please fix it!']
bob.offers = {
  "beer": 7,
  "shot": 10,
  "glass of wine": 12,
  "bottle of wine": 40,
  "mystery shot": 75
}

# Assign Characters to a room
crew_quaters.character = bob

# Init MAIN Variable
current_room = crew_quaters
running = True
backpack = []
money = 100

# ----- MAIN LOOP ----- #
print("""\
 __              _ _               
|  |   ___ ___ _| |_|___ ___       
|  |__| . | .'| . | |   | . |_ _ _ 
|_____|___|__,|___|_|_|_|_  |_|_|_|
                        |___|      
""")    
time.sleep(3)
os.system('clear')
print("""\

    ___    __                    __                     __
   /   |  / /_  ____ _____  ____/ /___  ____  ___  ____/ /
  / /| | / __ \/ __ `/ __ \/ __  / __ \/ __ \/ _ \/ __  / 
 / ___ |/ /_/ / /_/ / / / / /_/ / /_/ / / / /  __/ /_/ /  
/_/  |_/_.___/\__,_/_/ /_/\__,_/\____/_/ /_/\___/\__,_/   
                                                          
                                                        
""")
time.sleep(1.5)

while running:
  current_room.describe()

  command = input("> ").lower()
# move
  if command in ["north","south",'east','west']:
    current_room = current_room.move(command)
# Talk
  elif command == "talk":
    if current_room.character is not None:
      current_room.character.talk()
    else:
      print("There is no one here!")

# buy
  elif command == "buy":
    if current_room.character is not None:
      current_room.character.buy()

  