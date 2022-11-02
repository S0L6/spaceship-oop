from multiprocessing.sharedctypes import Value
import random

class Character():

    def __init__(self,name):
        # initialises the character object
        self.name = name
        self.description = None
        self.conversation = None

    def describe(self):
        # sends a description of the character to the terminal
        print(f'{self.name} is here, {self.description}')

    def hug(self):
        # the character response to a hug
        print(f"{self.name} doesnt want to hug you.")
    
    def fight(self):
        # the character responds to a threat
        print(f"{self.name} doesn't want to fight you.")

    def talk(self):
        # the character responds to a conversation
        if self.conversation is not None:
            if self.conversation == list:
                convochoice = random.choice(self.conversation)
                print(f"{self.name}: > {convochoice}")
            else:
                print(f"{self.name}: > {self.conversation}")
        else:
            print("The character doesn't want to talk to you.")

class Friend(Character):

    def __init__(self,name):
        # option1, option2, option3, option4, option5
        # Initilises teh friend object by calling the chracter init
        super().__init__(name)
        self.offers = {
            None: None,
            None: None,
            None: None,
            None: None,
            None: None
        }

    def buy(self, credits, backpack):
        # the friend offers to sell things
        offers = '\n'.join(f'{key}: {value}' for key, value in self.offers.items())
        print(offers)
        print(f"\nYou have " + str(credits) + " credits.")
        purchase = input('What do you want to buy? (Type <QUIT> to exit.) > ').lower()
        try:
            if credits >= self.offers[purchase]:
                credits = credits - self.offers[purchase]
                print("You bought " + (purchase) + " and have " + str(credits) + " credits.")
                backpack.append(str(purchase))
                return credits
            else:
                print("You don't have enough credits. HINT: Look around for more.")
        except:
            pass       
        
        


class Enemy(Character):

    num_of_enemy = 0

    def __init__(self,name):
        # initilise the enemy object by calling the character init
        super().__init__(name)
        self.weakness = None
        Enemy.num_of_enemy += 1
    
    def fight(self,item):
        if item == self.weakness:
            print(f"You strike {self.name} down with {item}.")
            Enemy.num_of_enemy -= 1
            return True
        else:
            print(f"{self.name} crushes you. Puny Adventurer.")
            return False
    
    def get_num_of_ennemy():
        # returns the amount of enemies remaining
        return Enemy.num_of_enemy