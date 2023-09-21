import random # To generate random items from a list 

fruits = ['APPLE', 'ORANGE', 'BANANA', 'PEACH']#list of fruits 
random_fruits = []# List of random fruits generated later
player_guess= []# List of fruits player enters later
attempts = 0 # Number of guesses
game = True

# Subprogram to generate random fruits
def fruitsrandomgenerator():
    for x in range(4):
        random_fruits.append(random.choice(fruits))
    print (random_fruits)
    
# Subprogram to showcase the cases below  
def cases(case1, case2):
    print('correct fruit in correct position:', case1)
    print('correct fruit in wrong position:', case2)



fruitsrandomgenerator()
print('_______________________')
print()
print(' WELCOME TO MASRERMIND')
print('_______________________')
print()
print('Guess the fruits from the available fruits below')
print('Fruits to choose from are: APPLE, ORANGE, BANANA, PEACH ')
print()
# Start of the game
while game:
    attempts += 1
    # Loop for player input and validation of player input
    while len(player_guess) != 4:
        player_fruits = input('Enter fruit of choice:').upper()
        if player_fruits not in fruits:
            print ('fruits available to enter: APPLE, ORANGE, BANANA, PEACH')
        else:
            player_guess.append(player_fruits)
    print ('Your Fruits are: ', player_guess)
    

    # Comparison between random fruits list and the player input list
    case1 = 0 
    case2 = 0 
    if random_fruits[0] == player_guess[0]: # Position of first fruit
        case1 += 1
    elif random_fruits[0] == player_guess[1] or random_fruits[0] == player_guess[2] or random_fruits[0] == player_guess[3]:
        case2 += 1
    if random_fruits[1] == player_guess[1]: # Position of second fruit
        case1 += 1
    elif random_fruits[1] == player_guess[0] or random_fruits[1] == player_guess[2] or random_fruits[1] == player_guess[3]:
        case2 += 1
    if random_fruits[2] == player_guess[2]: # Position of third fruit
        case1 += 1
    elif random_fruits[2] == player_guess[0] or random_fruits[2] == player_guess[1] or random_fruits[2] == player_guess[3]:
        case2 += 1
    if random_fruits[3] == player_guess[3]: # Position of fourth fruit
        case1 += 1
    elif random_fruits[3] == player_guess[0] or random_fruits[3] == player_guess[1] or random_fruits[3] == player_guess[2]:
        case2 += 1
        
    if player_guess == random_fruits:
        cases(case1, case2)
        print('_______________________________________________')
        print (' Congratulations you took',attempts,'gusses')
        break # End of the game if conditions are fulifiled
    
    # Allow the player to input another guess if they didn't guess correctly
    else:
        cases(case1, case2)
        print()
        print ('Wrong guess, try again')
        player_guess = []
