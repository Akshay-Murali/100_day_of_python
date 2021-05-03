# Sum of Even numbers

total = 0

# using the step we can step-up 2 numbers.
# similar to for (initialization;condition;i+2) in c

for i in range(2,102,2):
  total = total+i

print(f"Sum of even numbers between 2 & 100 is {total}")