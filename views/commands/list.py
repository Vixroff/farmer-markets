from model.commands.list import get_data


MODES = {
    '1': 'fmid',
    '2': 'marketname',
    '3': 'rate'
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


def show_output(markets: list):
    for market in markets:
        x = """
        Market №{fmid}
            "{marketname}"
        Rating: {rate}
        Address:
            {street}, {city}, {county}, {state}, {zip}
        Categories:
            {categories}
        Payments:
            {payments}
        Seasons:
            season1 - {season1} {season1_time}
            season2 - {season2} {season2_time}
            season3 - {season3} {season3_time}
            season4 - {season4} {season4_time}
        Media:
            youtube - {youtube}
            facebook - {facebook}
            website - {website}
            othermedia - {othermedia}
        \n
        """.format(**market)
        print(x)


def execute_list(args=None):
    status, answer = check_args(args)
    if status is True:
        mode, reverse = get_args(args)
        markets = get_data()
        if markets:
            markets = sorted(markets, key=lambda x: x[MODES.get(mode)], reverse=REVERSE.get(reverse))
            show_output(markets)
        else:
            print('No markets were found')
    else:
        print(answer)


if __name__ == "__main__":
    execute_list()
