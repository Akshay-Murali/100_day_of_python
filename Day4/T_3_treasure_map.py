#Treasure Map


# Creating 3 rows with tiles emoji

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

#creating a list in list variable map

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

# getting the position to put the treasure

position = int(input("Where do you want to put the treasure? "))


x = (position//10) 
y = (position - (x*10)) 


if x>=4 or y>=4:
 	print("Wrong Input")

else:
  	x-=1
  	y-=1

	map[x][y]="X"

  	print(f"{row1}\n{row2}\n{row3}")