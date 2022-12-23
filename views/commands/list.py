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
        return True, "Args are valid!"
    elif len(args) == 1 and args[0] in MODES:
        return True, "Args are valid!"
    elif len(args) == 2 and args[0] in MODES and args[1] in REVERSE:
        return True, "Args are valid!"
    elif len(args) > 2:
        return False, 'Oops! Too much arguments\nTry again!'
    elif len(args) >= 1 and args[0] not in MODES:
        return False, 'Oops! Wrong mode type\nTry again!'
    elif len(args) == 2 and args[1] not in REVERSE:
        return False, 'Oops! Wrong reverse type\nTry again!'


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


def make_list(mode, reverse):
    data = request("db/Markets.csv")
    for market in data:
        market['rating'] = 'No rating yet'
    result = sorted(data, key=lambda x: x[MODES.get(mode)], reverse=REVERSE.get(reverse))
    return result


def show_list(data):
    for row in data:
        print("FMID:{fmid}, MARKETNAME: {marketname}, RATING: {rating}".format(**row))


def list_console(args):
    arguments_validation = check_args(args)
    status = arguments_validation[0]
    answer = arguments_validation[1]
    if status is False:
        print(answer)
    else:
        mode, reverse = get_args(args)
        result = make_list(mode, reverse)
        show_list(result)


