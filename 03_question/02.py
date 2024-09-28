# Fruit Ripness checker.

import random
fruit = input("Enter the fruit ")

clr = ['Green' , 'Yellow' , 'Brown']

color = random.choice(clr)
print(color);

if fruit == 'banana' :
    if color == 'Green':
        print("Unrinpe Banaa")
    elif color == 'Yellow':
        print("ripe Banana")
    elif color == 'Brown':
        print("overripe Banana")
else:
    print("No data for this fruit ");