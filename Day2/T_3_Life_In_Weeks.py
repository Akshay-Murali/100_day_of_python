#Life in weeks

age = input("What is your current age?")

desired_age = int(input("what age do you want to calculate? "))

# days is 365 per year
# week is 52 per year
# month is 12 per year


age = desired_age-int(age)

ageindays = age*365
ageinweek = age*52
ageinmonth = age*12

# printing results !

print(f"You have {ageindays} days / {ageinweek} weeks, /{ageinmonth} months left to reach {desired_age} years.")


