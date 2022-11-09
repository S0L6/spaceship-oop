##### MAIN #####

# Modules
from character import Character, Friend, Enemy
from room import Room
from item import Item
from object import Object
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
nuclear_reactor.description = '''
                                    xxxxxxx
                               x xxxxxxxxxxxxx x
                            x     xxxxxxxxxxx     x
                                   xxxxxxxxx
                         x          xxxxxxx          x
                                     xxxxx
                        x             xxx             x
                                       x
                       xxxxxxxxxxxxxxx   xxxxxxxxxxxxxxx
                        xxxxxxxxxxxxx     xxxxxxxxxxxxx
                         xxxxxxxxxxx       xxxxxxxxxxx
                          xxxxxxxxx         xxxxxxxxx
                            xxxxxx           xxxxxx
                              xxx             xxx
                                  x         x
                                       x
Green liquid seeps from the large glass silo. Defening sirens blaring warning signals due to a radioactive leak.'''

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

air_lock.link_rooms(maintenance, "north")

#create items
lava_blade = Item('Lava Blade')
lava_blade.description = "a blade crafted from the molten core of Planet-5479B. It is stored in a flowing lava tube."
lava_blade.category = 'weapon'

shiny_crate = Item('Shiny crate')
shiny_crate.description = 'a crate that leaks light in the dark corner waiting to be raidied.'
shiny_crate.category = 'credits'

beer = Item('Beer')
beer.category = 'alcohol'

shot = Item('Shot')
shot.category = 'alcohol'

glassofwine = Item('Glass of Wine')
glassofwine.category = 'alcohol'

bottleofwine = Item('Bottle of Wine')
bottleofwine.category = 'alcohol'

mysteryshot = Item('Mystery Shot')
mysteryshot.category = 'alcohol'

toolbelt = Item("Tool Belt")
toolbelt.category = 'tool'

fire_extinguisher = Item('Fire Extinguisher')
fire_extinguisher.category = 'tool'

laser_cutter = Item('Laser Cutter')
laser_cutter = 'tool'

sake = Item("Sake")
sake.category = 'alchohol'

coke = Item("Coca-Cola")
coke.category = "drink"

lemonade = Item("Lemonade")
lemonade.category = "drink"

gingerbeer = Item('Ginger Beer')
gingerbeer.category = "drink"

pepsi = Item("Pepsi")
pepsi.category = "drink"

fanta = Item("Pepsi")
fanta.category = "drink"


# Create Characters
bob = Friend('Bob The Bartender')
bob.description = 'A friendly robotic bartender that sells alchohol.'
bob.conversation = ['What brings you onboard?', 'This ship is in critical condition please fix it!']
bob.offers = {
  beer.name : 7,
  shot.name : 10,
  glassofwine.name : 12,
  bottleofwine.name : 40,
  mysteryshot.name : 75
}

mechanic = Friend('The Mechanic')
mechanic.description = 'A mysterious entity willing to trade for his toolbelt.'
mechanic.conversation = ['This can help the repairs.', 'You need this belt fo later.', "If you don't stop the radiation leak it will destroy this planet."]
mechanic.offers = {
toolbelt.name : 150
}

the_mech = Enemy('The Mech')
the_mech.description = '''A huge robot mech that roams the engine room.
 _______             _______
|@|@|@|@|           |@|@|@|@|
|@|@|@|@|   _____   |@|@|@|@|
|@|@|@|@| /\_T_T_/\ |@|@|@|@|
|@|@|@|@||/\ T T /\||@|@|@|@|
 ~~~~/|~||~\/~T~\/~||~T~~T\~
   /_,|_| \(-(O)-)/ |_|__|/
  /~\      \\8_8//    |_ |_
 (O_O)  /~~[_____]~~\   [(@)|
       (  |       |  )    ~
      [~` ]       [ '~]
      |~~|         |~~|
      |  |         |  |
     _<\/>_       _<\/>_
    /_====_\     /_====_\
'''
the_mech.conversation = ['Brrt brt brrttttt', 'shu shuuuu brrrt', '*stomp* *stomp* *stomp* brrrt']
the_mech.weakness = 'lava blade'

# create objects
vendingmachine = Object("A Vending Machine")
vendingmachine.description = "pick what you want and it will dispense it."
vendingmachine.action = "buy"
vendingmachine.dict = {
  sake.name : 4,
  coke.name : 3,
  lemonade.name : 3,
  fire_extinguisher.name : 75,
  gingerbeer.name : 6,
  pepsi.name : 3,
  fanta.name : 3
}

# Assign Characters to a room
bar.character = bob
rengine_room.character = the_mech
maintenance.character = mechanic

# add items to a room
armoury.item = lava_blade
crew_quaters.item = shiny_crate

# add objects to a room
bridge.object = vendingmachine

# Init MAIN Variable
current_room = crew_quaters
running = True
backpack = []
credits = 100
drinkcount = 0
slownesscounter = 0
slowness = 0.5

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
   ___   __                __                 __
  / _ | / /  ___ ____  ___/ /__  ___  ___ ___/ /
 / __ |/ _ \/ _ `/ _ \/ _  / _ \/ _ \/ -_) _  / 
/_/ |_/_.__/\_,_/_//_/\_,_/\___/_//_/\__/\_,_/  
                                                
""")
time.sleep(1)
print("""\
   ____                      __   _    
  / __/__  ___ ________ ___ / /  (_)__ 
 _\ \/ _ \/ _ `/ __/ -_|_-</ _ \/ / _ \ 
/___/ .__/\_,_/\__/\__/___/_//_/_/ .__/
   /_/                          /_/    
""")
time.sleep(1)
print("""\
   ___     __              __              
  / _ |___/ /  _____ ___  / /___ _________ 
 / __ / _  / |/ / -_) _ \/ __/ // / __/ -_)
/_/ |_\_,_/|___/\__/_//_/\__/\_,_/_/  \__/                                              
""")
time.sleep(2)
# ----- MAIN LOOP ----- #
while running:
  current_room.describe(slowness)

  command = input("You > ").lower()
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
      credits = current_room.character.buy(credits, backpack)   

# backpack  
  elif command == "backpack":
    if backpack == []:
      print("\nYour backpack is empty")
    else:
      print(", ".join(backpack).capitalize())

  elif command == 'take':
    if current_room.item is not None:
      backpack.append(current_room.item)
      print(f"You put {current_room.item.name} into your backpack.")
      current_room.item = None
    else:
      print("There is nothing to take.")
  
  elif command == 'use':
    if backpack == []:
      print("Your backpack is empty.")
    else:
      print(", ".join(backpack))
      useitem = input("What item do you want to use? (Type <QUIT> to exit) > ")
      if useitem.category == 'alcohol':
        drinkcount = useitem.item_use()
        print(f"You used {useitem}.")
        if drinkcount == 5:
          print("You have drunk to much, passed out and died. Better luck next time!")
          running = False
        elif useitem.category == 'credits':
          credits = useitem.item_use()
  
  elif command == "interact":
    if current_room.object is not None:
      credits = current_room.object.randomiser(credits, backpack)