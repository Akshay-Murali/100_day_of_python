# Pizza Order app

print("Welcome to Python Pizza Deliveries!")

# Get's User Input for size , pepperoni and cheese preference.
# Uses .strip() to remove any space added by mistake and .upper to capitalise

size = input("What size pizza do you want? S, M, or L ").strip().upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").strip().upper()
extra_cheese = input("Do you want extra cheese? Y or N ").strip().upper()

# Setting Bill to 0

bill = 0

# Charging as per bill

if size == "S":
  bill = 15
elif size == "M":
  bill = 20
elif size == "L":
  bill = 25
else :
  print("Enter proper value!")

# Charging $2 for adding pepperoni to small pizza $3 for bigger size
if add_pepperoni == "Y":
  if size == "S":
  	bill += 2
  else:
  	bill += 3

# Charging for extra cheese if choosen

if extra_cheese == "Y":
  bill += 1

# printing the output
print(f"Your Total bill is: ${bill}")
