#Get the year Input

year = int(input("Which year do you want to check? "))

# Uses the logic if divisible by 4 , except by 100 , unless by 400 then leap year
# https://www.youtube.com/watch?v=xX96xng7sAE

if year%4 == 0 :

  if year%100 == 0:
  
    if year%400 == 0:
      print("Leap Year")
  
    else:
      print("Not a Leap Year")
  
  else:
    print("Leap Year")
else:
  print("Not a Leap Year")