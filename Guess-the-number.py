***"Guess-The-Number" game implimentation using SIMPLE GUI module***

import simplegui  #custom module by Rice University
import math
import random


# initializing global variables
low = 0
high = 100
secret_number = random.randrange(low, high)
remaining_guesses = math.ceil(math.log(high - low,2))

# helper function to start and restart the game
def new_game():
    global secret_number, remaining_guesses
    secret_number = random.randrange(low, high)
    remaining_guesses = math.ceil(math.log(high - low,2))

    print "\n"
    print "New game. Range is from", low, "to", high
    print "Number of remaining guesses is", int(remaining_guesses)

# defining event handlers for control panel
# button that changes range to range [0,100) and restarts
def range100():

    global high
    high = 100    
    new_game()
    
# button that changes range to range [0,1000) and restarts
def range1000():

    global high
    high = 1000
    new_game()
    
# main game logic 
def input_guess(guess):

    global secret_number, remaining_guesses
    remaining_guesses -= 1
    guess = int(guess)
    
    print ""
    print "Guess was", guess
    print "Number of remaining guesses is", int(remaining_guesses)
    
    if remaining_guesses > 0:
        if guess > secret_number:
            print "Lower!"
        elif guess < secret_number:
            print "Higher!"
        else:
            print "Correct!"
            new_game()
    else:
        if guess == secret_number:
            print "Correct!"
        else:
            print "You ran out of guesses. The number was", secret_number
        new_game()

    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game and start frame
new_game()
frame.start()
