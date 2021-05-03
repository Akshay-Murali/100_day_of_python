# High Score Finder

print("Welcome to high score finder")

marks = input("Enter the Marks: ").split()

high_score = 0

# loops through every score , when the current score is
# higher than high_score it replaces the high_score

for mark in marks:
  if int(mark) > high_score :
    high_score = int(mark)

print(f"High score is : {high_score}")