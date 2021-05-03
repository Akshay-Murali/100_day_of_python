#TIP CALCULATOR

print("Welcome to the Tip Calculator\n")

# Storing values of the bill amount, tip , and people in their respective data type.

bill = float(input("What is the total Bill $"))
tip  = int(input("What percent tip would you like to give "))
people = int(input("How many people to split the bill? "))

# simplifying the percentage formula 
# Example 20 percent of 300 is 300 * 20/100 and adding up with the principle it is 300 + 300 * 20/100
# ==> 300*1 + (300*20/100)
# ==> 300(1+.2) = 300*(1.2)
# so we can simply express it by 1.x to get the total , where x is the percentage.

#here ,say tip is 20 then 20/100 = .2 , plus 1 gives 1.2! 
tip = tip/100+1

#Calculating the split 

total = (bill * tip)/people

#rounding off to 2 decimal points
total = round(total, 2)

#formating the string and printing it
total = "{:.2f}".format(total)
print(total)