# Treasure Hunter Game.
# Ascii Art https://ascii.co.uk/art

print("""
   180   150W  120W  90W   60W   30W   000   30E   60E   90E   120E  150E  180
    |     |     |     |     |     |     |     |     |     |     |     |     |
90N-+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-90N
    |           . _..::__:  ,-"-"._        |7       ,     _,.__             |
    |   _.___ _ _<_>`!(._`.`-.    /         _._     `_ ,_/  '  '-._.---.-.__|
    |>.{     " " `-==,',._\{  \  / {)      / _ ">_,-' `                mt-2_|
60N-+  \_.:--.       `._ )`^-. "'       , [_/(                       __,/-' +-60N
    | '"'     \         "    _L        oD_,--'                )     /. (|   |
    |          |           ,'          _)_.\\._<> 6              _,' /  '   |
    |          `.         /           [_/_'` `"(                <'}  )      |
30N-+           \\    .-. )           /   `-'"..' `:._          _)  '       +-30N
    |    `        \  (  `(           /         `:\  > \  ,-^.  /' '         |
    |              `._,   ""         |           \`'   \|   ?_)  {\         |
    |                 `=.---.        `._._       ,'     "`  |' ,- '.        |
000-+                   |    `-._         |     /          `:`<_|h--._      +-000
    |                   (        >        .     | ,          `=.__.`-'\     |
    |                    `.     /         |     |{|              ,-.,\     .|
    |                     |   ,'           \   / `'            ,"     \     |
30S-+                     |  /              |_'                |  __  /     +-30S
    |                     | |                                  '-'  `-'   \.|
    |                     |/                                         "    / |
    |                     \.                                             '  |
60S-+                                                                       +-60S
    |                      ,/            ______._.--._ _..---.---------._   |
    |     ,-----"-..?----_/ )      __,-'"             "                  (  |
    |-..,(                  `-----'                                       `-|
90S-+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-90S
""")


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# Get's user input to go left or right , left continues , right or wrong input game ends
dir = input("You are in the middle of the ocean choose which direction to go Left or Right: ").strip().lower()

if dir == "left" :

	print("You have reached a unknown Island and it's dark\nWait for sunrise or start search:")
	reaction = input("Enter sunrise or start search: ").strip().lower()
  	
	if reaction == "sunrise":
    	
    	print("You have reached 3 house with different color door")
    	color = input("Choose between red, yellow or blue: ").strip().lower()
    	
    	if color == "red":
      		print("House is on Fire \nGame Over")
    	
    	elif color == "yellow":
      		print("Yaay! you have found the treasure!")
   	 	
   	 	elif color =="blue":
      		print("You got flushed out back into the sea\nGame over")
  	
  		else :
  			print("Wrong input the doors are locked\n Game Over")

  	elif reaction =="start search":
    	print("you fell into a pit and died\nGame over")
  
 	else:
    	print("Wrong Input Zeus threw a lightning bolt and killed you\n Game Over")


elif dir == "right":
  print("You got caught in high tide\nGame Over")


else:
  print("Wrong input a Kraken appeared and ate you along with your boat")


