# This code is for the AP CSP Mock Create Task
# Purpose: Guessing Game
# Constraints:
# Must Include:
  # --User defined function
  # --Loops
  # --Boolean (and, or, not, etc)
  # --Variables
  # --String methods (i.e. Concatenation, Indexing, Splicing)
  # --Comments indicating sources for coding ideas and purpose of each section
import time as t
from random import *
# Define all of the global variables needed
min_poss = 0
max_poss = 100
guess = 0
rand = randint(min_poss, max_poss)
orig = 5
life = 5
gmax = 0
gmin = 0
# Define a function to ask what game mode the user wants to play
def menu():
  global gmax
  global gmin
  print("""Welcome to the guessing game!
Select A Game Mode:
1: Easy (0-100)
2: Hard (0-400)""")
  choice = input("")
  # Check for input 1 or "easy"
  if choice == "1" or choice.lower() == "easy":
    gmax = 100
    gmin = 0
    ask(0, 100)
  # Check for input 2 or "hard"
  elif choice == "2" or choice.lower() == "hard":
    gmax = 400
    gmin = 0
    generate()
    ask(0,400)
  else:
    # Display an error if the value is not valid
    print("TypeError: Invalid Input. The input must be either 1 or 2")
    menu()
def generate():
  global rand
  seed = t.localtime().tm_sec # I used time to help with randomization as many pseudo random number generators use it as a seed value
  op = randint(0,1)
  lst = []
  bol = True

  while bol == True:
    lst.append(randint(0, seed))
    if len(lst) > 5:
      bol = False 
  for  item in lst:
    if op == 1:
      rand += item
    else:
      rand -= item
  rand = abs(rand)
# Define a function 'ask' that takes minimum and maximum as parameters
def ask(minimum, maximum):
  global guess

  # Set the value of 'guess' to the user's input
  guess = int(input("Enter your guess (%s-%s): " %(minimum, maximum)))

  # Check for invalid numbers
  if guess > maximum:
    print("Your guess is greater than the maximum possible random number. \n")
    ask(gmin, gmax)
  elif guess < minimum:
    print("Your guess is less than the minumum possible random number. \n")
    ask(gmin, gmax)
  else:
    check()
def ask_again(cond):
  global life
  if life == 0:
    print("You have run out of lives, the number was %s." %(rand))
    exit()
  global guess

  # Show different messages for different conditions
  if cond == "higher":
    print("Sorry! The number is higher than your guess of %s. Guesses left: %s \n" %(guess,life))
    guess = int(input("Enter another guess (%s-%s): " %(gmin, gmax)))
    if guess > gmax:
      print("Your guess is greater than the maximum possible random number. \n")
      ask(gmin, gmax)
    elif guess < gmin:
      print("Your guess is less than the minumum possible random number. \n")
      ask(gmin, gmax)
    else:
      life -= 1
      check()

  elif cond == "lower":
    print("Sorry! The number is lower than your guess of %s. Guesses left: %s \n" %(guess, life))
    guess = int(input("Enter another guess (%s-%s): " %(gmin, gmax)))
    if guess > gmax:
      print("Your guess is greater than the maximum possible random number. \n")
      ask(gmin, gmax)
    elif guess < gmin:
      print("Your guess is less than the minumum possible random number. \n")
      ask(gmin, gmax)
    else:
      life -= 1
      check()
# Define a function 'check' that takes no parameters    
def check():
  global life

  # Check if guess is equal to 'rand'
  if guess == rand:
    print("Correct! The number was %s." %(rand))
    life == life-orig
    return True
  elif guess < rand:
    ask_again("higher")
  elif guess > rand:
    ask_again("lower")
  else:
    print("Error: Your number is not an acceptable answer!")
menu()

    
