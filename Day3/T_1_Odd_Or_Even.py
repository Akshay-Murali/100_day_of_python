# Odd or Even

number = int(input("Which number do you want to check? "))

# uses modulo , gives reminder as 0 or 1 , 1 is true

reminder = number % 2
if reminder :
  print("This number is odd Number")
else :
  print("This is a even number")


