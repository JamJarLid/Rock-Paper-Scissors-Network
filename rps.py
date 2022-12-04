game_dict = {}


def get_key(val):
    global game_dict
    for key, value in game_dict:
        if val == value:
            return key

def choose_rps(player):
    global game_dict
    choice = input(f'''{player}, make your choice (1-3): 
    1. Rock
    2. Paper
    3. Scissors
    ''')
    if choice == '1':
        game_dict.update({player: 'Rock'})
        return 'Rock'
    elif choice == '2':
        game_dict.update({player: 'Paper'})
        return 'Paper'
    elif choice == '3':
        game_dict.update({player: 'Scissors'})
        return 'Scissors'
    else:
        choose_rps()

def rps_win():
    global game_dict
    if 'Rock' and 'Paper' in game_dict:
        return get_key('Paper')
    elif 'Paper' and 'Scissors' in game_dict:
        return get_key('Scissors')
    elif 'Rock' and 'Scissors' in game_dict:
        return get_key('Rock')
    else:
        return 'Tie'

def rps_round():
    global game_dict
    player_1 = input('Name: ')
    player_2 = input('Name: ')
    game_dict[player_1] = ''
    game_dict[player_2] = ''
    choose_rps(player_1)
    choose_rps(player_2)
    print(rps_win())

rps_round()

