

# BMI Calculator

print("Welcome to BMI Calculator")

# Collects user Height in Meter and Weight in KiloGram.

height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))

# Uses the formula Weight/(height*height) to give the BMI

bmi = int(weight/(height**2))

#using f string to print the String and int together

print(f"Your BMI is :{bmi}") 