#Fizz buzz generator

user_input = int(input("Enter the number till which you want to generate: "))

for i in range(1,user_input+1):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else: 
    print(i)