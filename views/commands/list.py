from model.csv.request import request


MODES = {
    '1': 'fmid',
    '2': 'marketname',
    '3': 'rating'
    }

REVERSE = {
    '+': False,
    '-': True
    }


def check_args(args):
    if not args:
        return True
    elif len(args) == 1 and args[0] in MODES:
        return True
    elif len(args) == 2 and args[0] in MODES and args[1] in REVERSE:
        return True
    elif len(args) > 2:
        print('Oops! Too much arguments\nTry again!')
        return False
    elif len(args) >= 1 and args[0] not in MODES:
        print('Oops! Wrong mode type\nTry again!')
        return False
    elif len(args) == 2 and args[1] not in REVERSE:
        print('Oops! Wrong reverse type\nTry again!')
        return False


def get_args(args):
    mode = '1'
    reverse = '+'
    if not args:
        return mode, reverse
    elif len(args) == 1:
        mode = args[0]
    elif len(args) == 2:
        mode = args[0]
        reverse = args[1]
    return mode, reverse


def make_list(args):
    if not check_args(args):
        return False
    data = request("db/Markets.csv")
    for market in data:
        market['rating'] = 'No rating yet'
    mode, reverse = get_args(args)
    result = sorted(data, key=lambda x: x[MODES.get(mode)], reverse=REVERSE.get(reverse))
    return result
