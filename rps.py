
def choose_rps():
    choice = input('''Make your choice (1-3): 
        1. Rock
        2. Paper
        3. Scissors
        ''')
    if choice == '1':
        return 'Rock'
    elif choice == '2':
        return 'Paper'
    elif choice == '3':
        return 'Scissors'
    else:
        choose_rps()

def rps_win(input_1, input_2):
    inputs = [input_1, input_2]
    if 'Rock' and 'Paper' in inputs:
        return 'Paper'
    elif 'Paper' and 'Scissors' in inputs:
        return 'Scissors'
    elif 'Rock' and 'Scissors' in inputs:
        return 'Rock'
    else:
        return 'Tie'

def rps_round():
    player_1 = choose_rps()
    player_2 = choose_rps()
    print(rps_win(player_1, player_2))

rps_round()

