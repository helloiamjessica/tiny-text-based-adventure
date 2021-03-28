print('''
   ================================================.
     .-.   .-.     .--.                         |
    | OO| | OO|   / _.-' .-.   .-.  .-.   .''.  |
    |   | |   |   \  '-. '-'   '-'  '-'   '..'  |
    '^^^' '^^^'    '--'                         |
===============.  .-.  .================.  .-.  |
               | |   | |                |  '-'  |
               | |   | |                |       |
               | ':-:' |                |  .-.  |
l42            |  '-'  |                |  '-'  |
==============='       '================'       |
''')
print("Welcome to 'Pacman'.")
print("Your mission is to not die.") 

left_or_right = input("OK, Pacman. Would you like to go right or left?\n").lower()
#left_or_right = left_or_right.lower()

if left_or_right == "right":
  print("What! Inky was right behind you. \nGame over.")
elif left_or_right == "left":
  wait_or_eat = input('Nice. Want to eat that huge pellet or wait a bit? \nChoose "wait" or "eat": ').lower()
else:
  print("That wasn't even a option.\nGame definitely over.")

if wait_or_eat == "eat":
  print("Good choice. But you died, sorry.\nGame Over.")
elif wait_or_eat == "wait":
  print('''

__________________|      |____________________________________________
     ,--.    ,--.          ,--.   ,--.
    |oo  | _  \  `.       | oo | |  oo|
o  o|~~  |(_) /   ;       | ~~ | |  ~~|o  o  o  o  o  o  o  o  o  o  o
    |/\/\|   '._,'        |/\/\| |/\/\|
__________________        ____________________________________________
                  |      |

''')
  ghost = input('Alright, now we\'re talkin\'. Which ghost do you think you can take on 1v1?? Cuz they\'re on your heels. \n"Pinky" or "Blinky" or "Clyde"?: ').lower()
else:
  print("Huh? No. Game Over.")

if ghost == "blinky":
  print("This guy's actually the ring leader. Your ass is grass. \nGame Over :( .")
elif ghost == "pinky":
  print("Queen of ambush attacks?! RIP & also Game Over.")
  print('''
        
                 mo / )
                 |/)\)
                  /\_
                  \__|=
                 (    )
                 __)(__
           _____/      \\_____
          |  _     ___   _   ||
          | | \     |   | \  ||
          | |  |    |   |  | ||
          | |_/     |   |_/  ||
          | | \     |   |    ||
          | |  \    |   |    ||
          | |   \. _|_. | .  ||
          |                  ||
          |  Pacman :(       ||
          |                  ||
  *       | *   **    * **   |**      **
   \))ejm97/.,(//,,..,,\||(,,.,\\,.((//
''')
elif ghost == "clyde":
  print("!!!")
  print('''
                                           88                       
  ,d                                       88                       
  88                                       88                       
MM88MMM 8b,dPPYba,  ,adPPYba,  8b,dPPYba,  88,dPPYba,  8b       d8  
  88    88P'   "Y8 a8"     "8a 88P'    "8a 88P'    "8a `8b     d8'  
  88    88         8b       d8 88       d8 88       88  `8b   d8'   
  88,   88         "8a,   ,a8" 88b,   ,a8" 88       88   `8b,d8'    
  "Y888 88          `"YbbdP"'  88`YbbdP"'  88       88     Y88'     
                               88                          d8'      
                               88                         d8'       
''')
  print("You juke Clyde! Clyde isn't too bright. You win.")
else:
  print("who? game over!")






#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload