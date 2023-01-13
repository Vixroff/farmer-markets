from model.commands.find import get_data


MODES = {
    '1': 'city',
    '2': 'state',
    '3': 'zip'
}


def check(args):
    if not args:
        return False, "No filters entered"
    elif len(args) % 2 != 0:
        return False, "Lost mode/value argument!"
    for arg in args[0::2]:
        if arg not in MODES.keys():
            return False, "Wrong type of mode!"
    return True, "Args is valid"


def get_filters(args):
    result = []
    for i in range(0, len(args), 2):
        arg = {}
        arg['column'] = MODES.get(args[i])
        arg['value'] = args[i + 1]
        result.append(arg)
    return result


def show_output(markets, filter):
    intro = "Filters: {column} - {value}".format(**filter)
    print(intro)
    if markets:
        for market in markets:
            x = "№{fmid}: \"{marketname}\"".format(**market)
            print(x)
        print('\n')
    else:
        print("No markets were found\n")


def execute_find(args):
    status, answer = check(args)
    if status is True:
        filters = get_filters(args)
        for filter in filters:
            markets = get_data(filter)
            show_output(markets, filter)
    else:
        print(answer)


if __name__ == "__main__":
    execute_find(('1', 'New York', '1', 'lhlh'))
