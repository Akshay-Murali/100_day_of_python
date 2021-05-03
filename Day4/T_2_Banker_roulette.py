#Banker's roulette

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")

$finds the length of the names and picks one randomly

length = len(names)-1 

random = random.randint(0,length)

print(f"{names[random]} is going to pay")