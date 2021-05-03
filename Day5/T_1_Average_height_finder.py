# Average_height_finder

student_heights = input("Input a list of student heights: ").split()

total = 0
i = 0

# for every input we calculate the total number of student 
#and their heights in total 
# note we can also use len() to calculate their height


for n in student_heights:
  i +=1
  total = total + int(n)

average = total /i

print(average)

