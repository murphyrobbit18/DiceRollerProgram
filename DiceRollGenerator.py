#This program is meant to give the user a random number based upon what dice and what amount of dice they choose.

import random

#Function to show the heading, initial comment and list. Will be put in the while statement so when the screen clears, this function will have the text remain.
def ProgramHeader ():
  print("---------------------------------------------------------------------------------------")
  print("                              Online Dice Roll Generator ")
  print("                               Created By Robin Murphy")
  print("---------------------------------------------------------------------------------------\n")

  print("\nWelcome to my dice roll generator. I can give you a random number based on which dice you want to roll from the given list. \n")
  
  ChoiceOfDice = ["d4","d6","d8","d10","d12","d20","d100"]

#This is a base zero list  
  number = 0

#As this is a base 0 list, the numbers displayed need to be increased by 1
  for Dice in ChoiceOfDice:
    number = number + 1
    print(number,".",Dice)

#This is a function to clear the screen
def ClearScreen():
  print("\033[H\033[J", end="")

#This is a function that prompts the user to press the enter button to clea the screen and pick another number
def RollAgain ():
 input("\nTo select another number to get an automated roll or to exit the program, please select enter.")

#The answer is set to true to have the loop continue
answer = True

#While the answer is true, the loop of the screen clearing the last answer, showing the question, and asking for user input wil continue
while answer == True:
  ClearScreen()
  ProgramHeader()
  print(" ")
  WhatDice = input("Select the number corresponding to the dice you want on the list. If you no longer want to get a roll, please type in a 0. \n\n")
  
#These statements correspond to which dice the user chose and gives a random number based on the perameters of the dice 
  if WhatDice == '1':
    print("\nThe random dice roll on your d4 is", random.randint(1,4))
    RollAgain ()

  elif WhatDice == '2':
    print("\nThe random dice roll on your d6 is", random.randint(1,6))
    RollAgain ()
    
  elif WhatDice == '3':
    print("\nThe random dice roll on your d8 is", random.randint(1,8))
    RollAgain ()
    
  elif WhatDice == '4':
    print("\nThe random dice roll on your d10 is", random.randint(1,10))
    RollAgain ()

  elif WhatDice == '5':
    print("\n The random dice roll on your d12 is", random.randint(1,12))
    RollAgain ()
  
  elif WhatDice == '6':
    print("\nThe random dice roll on your d20 is", random.randint(1,20))
    RollAgain ()
    
  elif WhatDice == '7':
    print("\nThe random dice roll on your d100 is", random.randint(1,100))
    RollAgain ()

#If the answer is zero, the loop will end  
  elif WhatDice == '0':
    answer = False
    
#If the user puts in an answer that is outside of the numbers 1-7 or they don't input a letter at all, they will be told it's invalid and be asked to put in another answer
  else:
    print("\nThis input is invalid.\n")
    RollAgain()

#The user is given a farewell as the loop ends 
print ("\nCome back anytime you forget your dice. Have a nice day.")