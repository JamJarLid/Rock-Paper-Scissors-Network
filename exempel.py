from threading import Thread
from datetime import datetime
from network import connect, send

# convert timestamp to iso date time format


def timestamp_to_iso(timestamp):
    return datetime.fromtimestamp(timestamp / 1000)\
        .isoformat().replace('T', ' ').split('.')[0]


def send_message():
    while True:
        send(input())


choices = {}


def react_on_messages(timestamp, user, message):
    global choices
    time = timestamp_to_iso(timestamp)
    print(f'\n{time} {user}\n{message}\n')
    print("Choose paper, rock or scissors (just write one alternative)")
    print("or just wait for the other player if you have made your choice")
    if message in ['paper', 'rock', 'scissors']:
        choices[user] = message
    # both players have chosen
    if len(choices) >= 2:
        # check who has won
        print(choices)
        print('Now print who has won')
        # then empty the dictionary choices


user = input('Your name: ')
channel = input('Channel to join or create: ')
# connect to (or create) a channel, with a user name
connect(channel, user, react_on_messages)
# start non-blocking thread to input and send messages
Thread(target=send_message).start()
