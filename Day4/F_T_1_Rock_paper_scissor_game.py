# Rock paper scissors Game


import random

print("Welcome to RPS game!")

print("Enter your choice , 0 for rock 1 for paper and 2 for scissors")


# generates Random computer input and get's user Input

user = int(input())

comp = random.randint(0,2)

# Ascii Art

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Checks for the user input and then comparing with computer choice prints result

if user==0 :

  if comp ==0:
    print("your choice:\n",rock,"Computer choice",rock)
    print("Draw!")
  elif comp == 1:
    print("your choice:\n",rock,"Computer choice",paper)
    print("Computer Win!")
  else:
    print("your choice:\n",rock,"Computer choice",scissors)
    print("You Won!")

elif user ==1 :

  if comp ==0:
    print("your choice:\n",paper,"Computer choice",rock)
    print("You Won!")
  elif comp == 1:
    print("your choice:\n",paper,"Computer choice",paper)
    print("draw!")
  else:
    print("your choice:\n",paper,"Computer choice",scissors)
    print("Computer Won!")

elif user ==2 :

  if comp ==0:
    print("your choice:\n",scissors,"Computer choice",rock)
    print("Computer Won!")
  elif comp == 1:
    print("your choice:\n",scissors,"Computer choice",paper)
    print("You Won!")
  else:
    print("your choice:\n",scissors,"Computer choice",scissors)
    print("Draw")

else:
  print("Wrong Input")