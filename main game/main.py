##### MAIN #####

# Modules
from character import Character, Friend, Enemy
from room import Room
from item import Item
from object import Object
import random, time
from os import system, name

  # defineclear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

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

outside = Room("Outside")
outside.description = 'Now there is an unexplored planet for you to explore good luck.'

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
armoury.link_rooms(cargo_hold, "east")

cargo_hold.link_rooms(life_support, "north")
cargo_hold.link_rooms(eco_cont, "east")
cargo_hold.link_rooms(power, "south")
cargo_hold.link_rooms(armoury, "west")

eco_cont.link_rooms(server_room, "north")
eco_cont.link_rooms(cargo_hold, "west")

nuclear_reactor.link_rooms(power, "west")

power.link_rooms(cargo_hold, "north")
power.link_rooms(solar_array, "east")
power.link_rooms(maintenance, "south")
power.link_rooms(nuclear_reactor, "west")

solar_array.link_rooms(power, "east")

lengine_room.link_rooms(maintenance, "west")

maintenance.link_rooms(power, "north")
maintenance.link_rooms(rengine_room, "east")
maintenance.link_rooms(air_lock, "south")
maintenance.link_rooms(lengine_room, "west")

rengine_room.link_rooms(maintenance, "east")

air_lock.link_rooms(maintenance, "north")
air_lock.link_rooms(outside, "south")

#create items
lava_blade = Item('Lava Blade')
lava_blade.description = "a blade crafted from the molten core of Planet-5479B. It is stored in a flowing lava tube."
lava_blade.category = 'weapon'

bugspray = Item('Bug Spray')
bugspray.description = 'A limited edition bug spray that apparently kills anything. Certain death is guaranteed when it comes into contact with skin.'
bugspray.category = 'weapon'

shiny_crate = Item('Shiny crate')
shiny_crate.description = 'a crate that leaks light in the dark corner waiting to be raidied'
shiny_crate.category = 'credits'

pouch = Item("Pouch")
pouch.category = 'credits'

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
laser_cutter.category = 'tool'

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

garden_hoe = Item("Gardening Hoe")
garden_hoe.category = "tool"


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
toolbelt.name : 150,
pouch.name : 40
}

rob = Friend("Rob the Gardener")
rob.description = 'A robot that has lost his way. Maybe he was running from something?'
rob.conversation = ['My laser cutter could be handy?', "Whatever you do do't go into the eco room!", "The vines have gotten out of control since the reactor went into meltdown."]
rob.offers = {
  laser_cutter.name : 200,
  garden_hoe.name : 20
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

cockroach = Enemy('The Mutated Cockroach')
cockroach.description = 'A giant mutated cockroach climbs the walls'
cockroach.weakness = 'bug spray'

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

creditsmultiplier = Object("A Credits Multiplier")
creditsmultiplier.description = 'want to double, triple or even tenfold your credits?'
creditsmultiplier.action = 'gamble'

# Assign Characters to a room
bar.character = bob
rengine_room.character = the_mech
maintenance.character = mechanic
defense_room.character = rob
eco_cont.character = cockroach

# add items to a room
armoury.item = lava_blade
crew_quaters.item = shiny_crate
bridge.item = bugspray

# add objects to a room
bridge.object = vendingmachine
server_room.object = creditsmultiplier

# Init MAIN Variable
current_room = crew_quaters
running = True
backpack = []
credits = 100
drinkcount = 0
slownesscounter = 0
slowness = 0.5
reactorstatus = 0

print("""\
 __              _ _               
|  |   ___ ___ _| |_|___ ___       
|  |__| . | .'| . | |   | . |_ _ _ 
|_____|___|__,|___|_|_|_|_  |_|_|_|
                        |___|      
""")    
time.sleep(3)
clear()
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
time.sleep(1.5)
# ----- MAIN LOOP ----- #
while running:
  current_room.describe(slowness)

  command = input("You > ").lower()

# move
  if command in ["north","south",'east','west']:
    # Checking if reactor core has been fixed to be able to go outside
    if current_room == maintenance:
      if command == 'south':
        if reactorstatus == 1:
          if Enemy.get_num_of_ennemy() == 0:
            clear()
            print("You open the Air Lock with a hiss. A new world awaits. Good luck fellow explorer. Your journey is just beginning.")
            running = False
      else:
        current_room = current_room.move(command)
    else:
      current_room = current_room.move(command)

# Talk
  elif command == "talk":
    if current_room.character is not None:
      current_room.character.talk()
    else:
      print("There is no one here!")

# Fixing the nuclear reactor
  elif command == "fix":
    if current_room == nuclear_reactor:
      if "fire extinguisher" and "laser cutter" and "tool belt" in backpack:
        print("You contained the leak and stopped the reactor from overloading now all you need is to go outside.")
        reactorstatus = 1
      else:
        print("You don't have the right items. Try and find some tools.")
        time.sleep(0.5)
        pass
    else:
      print("You aren't in the right room. Try talking to some people to find out where to go.")
      time.sleep(0.5)
      pass

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

#  elif command == 'use':
#    if backpack == []:
#      print("Your backpack is empty")
#    else:
#      useitem = input("What item do you want to use? (Type <QUIT> to exit ) > ").lower()
#      itemcategory = ''
#      available_items = []
#      for item in backpack:
#        available_items.append(item.name)
#        if useitem in available_items:
#          itemcategory = useitem.item_use(itemcategory)
#          print("sucess")
#        else:
#          print("fail")



        

#  elif command == 'use':
#    if backpack == []:
#      print("Your backpack is empty.")
#    else:
#      print(", ".join(backpack))
#      
#      available_items = []
#      for item in backpack:
#        available_items.append(item.name)
#      if useitem in available_items:
#        if item.category == 'alcohol':
#          drinkcount = useitem.item_use(backpack, drinkcount)
#          print(f"You used {useitem}.")
#          if drinkcount == 5:
#            print("You have drunk to much, passed out and died. Better luck next time!")
#            running = False
#        elif item.category == 'credits':
#          credits = useitem.item_use(backpack, credits)
#          print(f"You used {useitem}.")
#        elif item.category == 'drink':
#          slownesscounter = useitem.item_use(backpack, slownesscounter)
#          if slownesscounter == 3:
#            slowness = 1
#            print("You feel lethargic you now move rooms slower.")
  
  elif command == "interact":
    if current_room.object is not None:
      credits = current_room.object.objectfunction(credits, backpack)

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
              else:
                running = False
          else:
              print(f"You don't have {weapon}.")
              print(f"{current_room.character.name} strikes you down. GG")
              running = False
      else:
         print("There is no one to fight.")
  
  elif command == 'quit':
    print('See you next time.')
    running = False
  
  elif command == 'help':
    clear()
    print("""
 You woke up on this mysterious space ship and need to get out. 
 But you need to fix the reactor core before it goes critical. 
 You can find the equipment you need on the ship in vending machines and from characters. 
 Then you need to escape to the airlock and gain access to the outside world.
    """)
    time.sleep(5)
    print("""
    Commands:
    - Help
    - Quit
    - North
    - East
    - South
    - West
    - Fix (Reactor Core)
    - Talk
    - Fight
    - Buy
    - Take (Items)
    - Backpack
    - Interact (Objects)
    """)
    time.sleep(5)
