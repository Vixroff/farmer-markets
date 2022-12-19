from model.csv.request import request, filter_data


MODES = {
    '1': 'city',
    '2': 'state',
    '3': 'zip'
}


def check(args):
    if not args:
        print("No filters entered")
        return False
    elif len(args) % 2 != 0:
        print("Lost mode/value argument\nCheck this out!")
        return False
    for arg in args[0::2]:
        if arg not in MODES:
            print("Wrong type of mode!")
            return False
    return True


def get_args(args):
    result = []
    for i in range(0, len(args), 2):
        arg = {}
        arg['column'] = MODES.get(args[i])
        arg['value'] = args[i+1]
        result.append(arg)
    return result


def find_by_city(_filter):
    cities_data = request("db/Cities.csv")
    addresses_data = request("db/Addresses.csv")
    markets_data = request("db/Markets.csv")
    city = filter_data(cities_data, _filter)
    if not city:
        print("No markets in this city")
        return False
    filter_to_addresses = {'column': 'id_city', 'value': city[0]['id_city']}
    address = filter_data(addresses_data, filter_to_addresses)
    filter_to_markets = {'column': 'fmid', 'value': address[0]['fmid']}
    markets = filter_data(markets_data, filter_to_markets)
    return markets


def find_by_state(_filter):
    states_data = request("db/States.csv")
    addresses_data = request("db/Addresses.csv")
    markets_data = request("db/Markets.csv")
    state = filter_data(states_data, _filter)
    if not state:
        print("No markets in this state")
        return False
    filter_to_addresses = {'column': 'id_state', 'value': state[0]['id_state']}
    address = filter_data(addresses_data, filter_to_addresses)
    filter_to_markets = {'column': 'fmid', 'value': address[0]['fmid']}
    markets = filter_data(markets_data, filter_to_markets)
    return markets


def find_by_zip(_filter):
    zips_data = request("db/Zips.csv")
    markets_data = request("db/Markets.csv")
    _zip = filter_data(zips_data, _filter)
    if not _zip:
        print("No markets on this zip code")
        return False
    filter_to_markets = {'column': 'id_zip', 'value': _zip[0]['id_zip']}
    markets = filter_data(markets_data, filter_to_markets)
    return markets
    

def make_find(args):
    if not check(args):
        return False
    result = []
    args = get_args(args)
    for arg in args:
        if arg['column'] == 'city':
            markets = find_by_city(arg)
        elif arg['column'] == 'state':
            markets = find_by_state(arg)
        elif arg['column'] == 'zip':
            markets = find_by_zip(arg)
        if markets:
            response = {'mode': arg['column'], 'value': arg['value']}
            response['markets'] = markets
            result.append(response)
    return result


if __name__ == "__main__":
    print("TEST 1")
    result = make_find(['2', 'Virginia'])
    if result:
        for filters in result:
            for market in filters['markets']:
                print(market['fmid'], market['marketname'])
    print("\n")
    print("TEST 2")
    result = make_find(['2', 'Virginia', '1', 'Miami', '3', '04073'])
    if result:
        for filters in result:
            for market in filters['markets']:
                print(market['fmid'], market['marketname'])
    print("\n")
    print("TEST 3")
    result = make_find(['lolo'])
    if result:
        for filters in result:
            for market in filters['markets']:
                print(market['fmid'], market['marketname'])
    print("\n")
    print("TEST 4")
    result = make_find(['1', 'lolo'])
    if result:
        print(result)
        for filters in result:
            for market in filters['markets']:
                print(market['fmid'], market['marketname'])          
