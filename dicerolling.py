import random

kapil = True

while kapil:
    print(random.randint(1,6))
    another_roll = input (" Do you want roll the dice again? (y/n): ")
    if another_roll.lower() == "y":
        continue
    else:
        break