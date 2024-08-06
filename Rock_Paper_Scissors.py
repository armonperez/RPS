import random

def play():

    user = input("'r' for rock , 's' for scissors , 'p' for paper")
    computer = random.choice (['r', 'p', 's'])

    if user == computer:
        return ' It is a tie'
    
    #r > s, s > p, p > r
    if  is_win(user, computer):
        return 'You won!'
    
    return 'You Lost!'
def is_win(player, opponent):
    # returns true if the player wins

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
print(play())