#Love Calculator
#Uses the logic of https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love

# get's input of the name

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# creates two variable to calculate the score

ten_place = 0
one_place = 0

#combining both of their name for easier calculation

totalname = name1+name2 .strip().lower()

ten_place=totalname.count("t") + ten_place
ten_place=totalname.count("r") + ten_place
ten_place=totalname.count("u") + ten_place
ten_place=totalname.count("e") + ten_place

ten_place = ten_place * 10

one_place=totalname.count("l") 
one_place=totalname.count("o") + one_place
one_place=totalname.count("v") + one_place
one_place=totalname.count("e") + one_place

score = ten_place+one_place

#based on the score gives a description!

if score <10 or score>90 :
  print(f"Your score is {score}, you go together like coke and mentos.")

elif score > 40 and score <50 :
  print(f"Your score is {score}, you are alright together.")

else:
  print(f"Your score is {score}.")