# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import math
import random
import simplegui

x_num = 0
no_range = 100
rem_guess = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global x_num, no_range, rem_guess
    rem_guess = int(math.ceil(math.log((no_range - 0), 2)))
    x_num = random.randrange(0, no_range)
    print "\nrange is from 0 to", range
    print "Remaining guesses are...", rem_guess              
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range = 100             
    new_game()
                 
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range = 1000
    new_game()
                 
def input_guess(guess):
    global rem_guess
    print "\n guess was...", guess
    guess = int(guess)
    rem_guess = rem_guess - 1
    print "No. of remaining guess is...", rem_guess             
    
    # main game logic goes here	
    if rem_guess > 0 :
       if guess > x_num :          
          print "Lower"
       elif guess < x_num :
          print "Higher"
       else :
          print "Correct"
          new_game()
    else:
       if guess == x_num:
          print "Correct"
       else:
          print "Out of guesses.Number was..", x_num       
       new_game() 

# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)                 
frame.add_input("Enter a guess:", input_guess, 200)
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
