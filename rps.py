def choose_rps(player):
    choice = input(f'''{player}, make your choice (1-3): 
    1. Rock
    2. Paper
    3. Scissors
    ''')
    if choice == '1':
        send(play=(player, 'Rock'))
    elif choice == '2':
        send(play=(player, 'Paper'))
    elif choice == '3':
        send(play=(player, 'Scissors'))
    else:
        choose_rps()

def rps_win():
    
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

