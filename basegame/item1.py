# items

class Item():

    def __init__(self,name):
        # init the Item object
        self.name = name.lower()
        self.description = None

    def describe(self):
        # prints the description of itme to the terminal
        print(f"You see {self.name} in the room. It is {self.description}.")