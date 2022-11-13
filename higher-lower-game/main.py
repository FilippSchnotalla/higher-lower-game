from random import choice
from game_data import data
import art

score = 0

while(True):
    a = choice(data)
    b = choice(data)
    
    print(art.logo)
    
    print('Compare A: {0}, a {1}, from {2}.'.format(a['name'], a['description'], a['country']))
    
    print(art.vs)
    
    print('Against B: {0}, a {1}, from {2}.'.format(b['name'], b['description'], b['country']))
    
    print() 
    
    while(True):
        user_input = input('Who has more followers? Type "A", or "B": ')
        if user_input.lower() == 'a':
            if a['follower_count'] > b['follower_count']:
                score += 1
            else:
                print('No, that was wrong.')
                print('You have finished with a score of: {0}'.format(score))
                exit()
            break
        if user_input.lower() == 'b':
            if b['follower_count'] > a['follower_count']:
                score += 1
            else:
                print('No, that was wrong.')
                print('You have finished with a score of: {0}'.format(score))
                exit()
            break
        print('Please Type "A" or "B".')
        
    print()