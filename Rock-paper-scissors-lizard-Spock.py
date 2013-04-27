import random

def number_to_name(number):
    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "paper"
    elif (number == 3):
        return "lizard"
    elif (number == 4):
        return "scissors"
    else :
        return "wrong number"
    
def name_to_number(name):
    if (name == "rock"):
        return 0
    elif (name == "Spock"):
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    elif (name == "scissors"):
        return 4
    else :
        return "wrong name"
   
def rpsls(name): 
    player_number = name_to_number(name)
    comp_number = random.randrange(0,5)
    
    diff = (player_number - comp_number) % 5
    
    if (diff == 1 or diff == 2):
        winner = "Player wins!"
    elif (diff == 3 or diff == 4):
        winner = "Computer wins!"
    else :
        winner = 'Player and computer tie!'    
        
    comp_name = number_to_name(comp_number)
    
    print ''
    print 'Player chooses ' + name
    print 'Computer chooses ' + comp_name
    print winner
    
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
