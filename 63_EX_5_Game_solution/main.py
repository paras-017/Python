import random
user = input('Choose : Snake, Water or Gun to Start the game\n')
computerObj = {'-1':'Snake',
                                '0':'Water',
                                '1':'Gun'}

r_num = random.randint(-1,1)
computer = computerObj[f'{r_num}']

def game():
    if(user == computer): return 'Draw'
    if((user == 'Snake' and computer =='Water' ) or (user == 'Water' and computer =='Gun') or (user == 'Gun' and computer =='Snake' )): return 'User is the winner'
    else: return 'Computer wins'

print(game())
print(computer)