credits = 100
backpack = []

dict = {
  "beer": 7,
  "shot": 10,
  "glass of wine": 12,
  "bottle of wine": 40,
  "mystery shot": 75
}
while True:
  command = input("> " ).lower()
  if command == "buy":
    offers = '\n'.join(f'{key}: {value}' for key, value in dict.items())
    print(offers)
    print(f"\n You have " + str(credits) + " credits.")
    purchase = input('What do you want to buy? > ')
    if credits >= dict[purchase]:
        credits -= dict[purchase]
        print("You bought " + (purchase) + " and have " + str(credits) + " credits.")
        backpack.append(str(purchase))
  if command == "backpack":
    print(", ".join(backpack))