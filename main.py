from threading import Thread
from datetime import datetime
from network import connect, send

game_dict = {}

def timestamp_to_iso(timestamp):
    return datetime.fromtimestamp(timestamp / 1000)\
        .isoformat().replace('T', ' ').split('.')[0]


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


def react_on_messages(timestamp, user, message):
    time = timestamp_to_iso(timestamp)
    print(f'\n{time} {user}\n{message}\n')

user = input('Your name: ')
channel = input('Channel to join or create: ')

connect(channel, user, react_on_messages)
game_dict.update(user, '')

