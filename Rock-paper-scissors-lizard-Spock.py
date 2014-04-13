# Rock-paper-scissors-lizard-Spock template
import random
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# converts name-string to number
def name_to_number(name):
    if(name == 'rock'):
        return 0
    elif(name == 'Spock'):
        return 1
    elif(name == 'paper'):
        return 2
    elif(name == 'lizard'):
        return 3
    elif(name == 'scissors'):
        return 4
    else:
        print "name doesn't match"
    

#converts name-int to strings
def number_to_name(number):
    if(number == 0):
        return "rock"
    elif(number == 1):
        return "Spock"
    elif(number == 2):
        return "paper"
    elif(number == 3):
        return "lizard"
    elif(number == 4):
        return "scissors"
    else:
        print "no matches for number"

    

def rpsls(player_choice): 

    print "\n"
    
    print "Player chooses "+ player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    
    # compute difference of comp_number and player_number modulo five
    difference_of_players = (player_number - comp_number) %5

    # determining winner
    if(difference_of_players == 1 or difference_of_players == 2):
        print "Player wins!"
    elif(difference_of_players == 3 or difference_of_players == 4):
        print "Computer wins!"
    else:
        print "Player and computer tie!" 
        
# TEST CASSES
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


