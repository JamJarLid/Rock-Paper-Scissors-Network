from threading import Thread
from datetime import datetime
from network import connect, send

def get_key(val, dict):
    global choices
    for key, value in dict.items():
        if val == value:
            return key

# convert timestamp to iso date time format
def timestamp_to_iso(timestamp):
    return datetime.fromtimestamp(timestamp / 1000)\
        .isoformat().replace('T', ' ').split('.')[0]


def react_on_messages(timestamp, user, message):
    time = timestamp_to_iso(timestamp)
    print(f'\n{time} {user}\n{message}\n')

def choose_rps():
    choice = input(f'''{user}, make your choice (1-3): 
    1. Rock
    2. Paper
    3. Scissors
    ''')
    if choice == '1':
        send('Rock')
    elif choice == '2':
        send('Paper')
    elif choice == '3':
        send('Scissors')
    else:
        choose_rps()

def rps_win(dict):
    if 'Rock' in list(dict.values()) and 'Paper' in list(dict.values()):
        return get_key('Paper', dict)
    elif 'Paper' in list(dict.values()) and 'Scissors' in list(dict.values()):
        return get_key('Scissors', dict)
    elif 'Rock' in list(dict.values()) and 'Scissors' in list(dict.values()):
        return get_key('Rock', dict)
    else:
        return 'Tie'

choices = {}

def rps_round(timestamp, user, message):
    global choices
    if message in ['Paper', 'Rock', 'Scissors']:
        choices[user] = message
        if len(choices) == 2:
            winner = rps_win(choices)
            if winner == 'Tie':
                win_message = f'The match is a Tie!'
                react_on_messages(timestamp, user, win_message)
            else:
                win_message = f'The winner is {winner}!'
                react_on_messages(timestamp, user, win_message)
    else:
        react_on_messages(timestamp, user, message)


user = input('Your name: ')
channel = input('Channel to join or create: ')
# connect to (or create) a channel, with a user name
connect(channel, user, rps_round)
# start non-blocking thread to input and send messages
Thread(target = choose_rps).start()