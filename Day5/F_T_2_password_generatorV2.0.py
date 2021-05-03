#Password Generator Project

import random

# initialization

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pchoice = ["letters","numbers","symbols"]
pwd = ''

print("Welcome to the PyPassword Generator!")

#user_input

char= int(input("How many characters would you like in your password?\n")) 
smbls = int(input(f"How many symbols would you like?\n"))
nbrs = int(input(f"How many numbers would you like?\n"))

#finding letters (chars are inclusive of letters, symbols and numbers)

letter = char - (smbls + nbrs)

# looping the length of char to generate that length of chars

for i in range(0,char):

  # checking if the smbls (or) nmbrs (or) letter is 0 to remove it from the choice

  if smbls == 0:
    if "symbols" in pchoice:
      pchoice.remove("symbols")
  if nbrs == 0:
    if "numbers" in pchoice:
      pchoice.remove("numbers")
  if letter == 0:
    if "letters" in pchoice:
      pchoice.remove("letters")
      
  # creating choice to choose from the p choice =>["letters","numbers","symbols"]    
  choice = random.randint(0,len(pchoice)-1)
  
  #generates based on choice and decrease the respective variables

  if pchoice[choice] == "symbols":
    rchoice = random.randint(0,len(symbols)-1)
    pwd = pwd+symbols[rchoice]
    smbls -= 1
    
  elif pchoice[choice] == "numbers":
    rchoice = random.randint(0,len(numbers)-1)
    pwd = pwd+numbers[rchoice]
    nbrs -= 1

  elif pchoice[choice]=="letters":
    rchoice = random.randint(0,len(letters)-1)
    pwd = pwd+letters[rchoice]     
    letter -= 1

print(f"your password is : {pwd}")