from config import Config


from model.csv.request import request, filter_data


MODES = {
    '1': 'city',
    '2': 'state',
    '3': 'zip'
}


DB_PATH = {
    'city': Config.CITIES,
    'zip': Config.ZIPS,
    'state': Config.STATES
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
        arg['value'] = args[i+1]
        result.append(arg)
    return result


def get_markets(filter):
    result = []
    item = filter['column']
    markets_data = request(Config.MARKETS)
    addresses_data = request(Config.ADDRESSES)
    items_data = request(DB_PATH[item])
    item_data = filter_data(items_data, filter)
    if item_data:
        filter_to_addresses = {'column': f'id_{item}', 'value': item_data[0][f'id_{item}']}
        addresses = filter_data(addresses_data, filter_to_addresses)
        for address in addresses:
            filter_to_markets = {'column': 'fmid', 'value': address['fmid']}
            markets = filter_data(markets_data, filter_to_markets)
            result += markets
        return result


def make_find(filters):
    result = []
    for filter in filters:
        response = {'mode': filter['column'], 'value': filter['value']}
        markets = get_markets(filter)
        response['markets'] = markets
        result.append(response)
    return result


def show_find(data):
    for row in data:
        print("\n")
        print(f"Searching parametres: {row['mode']} - {row['value']}")
        if row.get('markets'):
            for market in row['markets']:
                print(f"{market['fmid']} - {market['marketname']}")
        else:
            print(f'No markets were found')
        print("\n")


def find_console(args):
    arguments_validation = check(args)
    status = arguments_validation[0]
    answer = arguments_validation[1]
    if status is False:
        print(answer)
    else:
        filters = get_filters(args)
        result = make_find(filters)
        show_find(result)


if __name__ == "__main__":
    print("TEST 1")
    find_console(['2', 'California'])
    print("TEST 2")
    find_console(['2', 'Virginia', '1', 'Miami', '3', '04073'])
    print("TEST 3")
    find_console(['lolo'])
    print("TEST 4")
    find_console(['5', 'lolo'])
