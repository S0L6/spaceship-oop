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
            if self.conversation == dict:
                convochoice = random.choice(list(self.conversation.values()))
                print(f"{self.name}: > {convochoice}")
            else:
                print(f"{self.name}: > {self.conversation}")
        else:
            print("The character doesn't want to talk to you.")

class Friend(Character):

    def __init__(self,name):
        # Initilises teh friend object by calling the chracter init
        super().__init__(name)

    def buy(self):
        # the friend responds to the hug
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