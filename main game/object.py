import random

class Object():

    def __init__(self,name):
        # inti the object object
        self.name = name
        self.description = None
        self.dict = {}
        self.action = None
    
    def describe(self):
        print(f"{self.name} is in the corner, {self.description}")

    def randomiser(self, credits, backpack):
        options = '\n'.join(f'{key}: {value}' for key, value in self.dict.items())
        print(options)
        print(f"\nYou have " + str(credits) + " credits.")
        function = input(f'What do you want to {self.action}? (Type <QUIT> to exit.) > ').lower()
        try:
            if credits >= self.dict[function]:
                credits = credits - self.dict[function]
                print("You bought " + (function) + " and have " + str(credits) + " credits.")
                backpack.append(str(function))
                return credits
            else:
                print("You don't have enough credits. HINT: Look around for more.")
        except:
            pass

