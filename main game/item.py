# items
import random

class Item():

    def __init__(self,name):
        # init the Item object
        self.name = name.lower()
        self.description = None
        self.category = None

    def describe(self):
        # prints the descrisption of itme to the terminal
        print(f"You see {self.name} in the room. It is {self.description}.")
    
    def item_use(self,itemcategory):
        self.category = itemcategory

        #if self.category == 'alcohol':
        #    drinkcount += 1
        #    print(f"You drunk {self.name}")
        #    backpack.remove(self.name)
        #    return drinkcount
        #elif self.category == 'credits':
        #    credits += random.randint(1, 1000)
        #    backpack.remove(self.name)
        #    return credits
        #elif self.category == 'weapon' or 'tool':
        #    print(f"You pull out your weapon observe the fine craftmenship of (the) {self.name}")
        #elif self.category == 'drink':
        #    slownesscounter += 1
        #    backpack.remove(self.name)
        #    return slownesscounter
