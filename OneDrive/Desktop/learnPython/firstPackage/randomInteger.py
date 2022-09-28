import random

difficulty = 3

health = 50
potion_health = random.randint(25,50)/difficulty
#This returns a float

health = (int)(health + potion_health)
#This is type casting

print(potion_health, health)


