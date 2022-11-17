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

    def objectfunction(self, credits, backpack):
        if self.action == 'buy':
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
        elif self.action == 'gamble':
            try:
                amount = int(input(f"You have {credits} credits how much do you want to gamble? (Type <QUIT> to exit.) > "))
                randomnum = random.randint(1,2)
                if amount > credits:
                    print("You don't have enough credits.")
                    pass
                if randomnum == 1:
                    randomnum = random.randint(1,100)
                    if randomnum <= 40:
                        credits += amount*2
                        print(f"You win! Your bet have been multiplied by 2. You now have {credits} credits.")
                        return credits
                    elif randomnum <= 65:
                        credits += amount*3
                        print(f"You win! Your bet have been multiplied by 3. You now have {credits} credits.")
                        return credits
                    elif randomnum <= 85:
                        credits += amount*5
                        print(f"You win! Your bet have been multiplied by 5. You now have {credits} credits.")
                        return credits
                    elif randomnum <= 100:
                        credits += amount*10
                        print(f"You win! Your bet have been multiplied by 10. You now have {credits} credits.")
                        return credits
                elif randomnum == 2:
                    credits -= amount
                    print(f"You lose {amount}. Better luck next time. You have {credits} credits.")
                    return credits
            except:
                pass
