choices = {'espen': 'Rock',
            'hanna': 'Paper'}

def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key

def rps_win(dict):
    if 'Rock' in list(dict.values()) and 'Paper' in list(dict.values()):
        return get_key('Paper', dict)
    elif 'Paper' in list(dict.values()) and 'Scissors' in list(dict.values()):
        return get_key('Scissors', dict)
    elif 'Rock' in list(dict.values()) and 'Scissors' in list(dict.values()):
        return get_key('Rock', dict)
    else:
        return 'Tie'


print(len(choices))