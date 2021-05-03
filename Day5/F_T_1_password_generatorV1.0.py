#Password Generator
import random

#variables in list and password string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ''

#getting inputs

print("Welcome to the PyPassword Generator!")
char= int(input("How many letters would you like in your password?\n")) 
smbls = int(input(f"How many symbols would you like?\n"))
nbrs = int(input(f"How many numbers would you like?\n"))

#calculating the number of letters to be printed from the total length.

char=char-(smbls+nbrs)

#generating password

for i in range(0,char):
  choice = random.randint(0,len(letters)-1)
  password = password+letters[choice]
for i in range(0,smbls):
  choice = random.randint(0,len(symbols)-1)
  password = password+symbols[choice]
for i in range(0,nbrs):
  choice = random.randint(0,len(numbers)-1)
  password = password+numbers[choice]

print(password)