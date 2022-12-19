from model.csv.request import request, filter_data


def check(args):
    if len(args) != 1:
        print("Please, enter your FMID index correctly!")
    zip_code = args[0]
    if len(zip_code) != 7:
        print("Invalid FMID code!")
        return False
    else:
        return True


def get_full_address(market: dict):
    market['address'] = {}
    addresses_data = request("db/Addresses.csv")
    cities_data = request("db/Cities.csv")
    counties_data = request("db/Counties.csv")
    states_data = request("db/States.csv")
    zips_data = request("db/Zips.csv")
    _filter_to_address = {'column': 'fmid', 'value': market['fmid']}
    address = filter_data(addresses_data, _filter_to_address)[0]
    _filter_to_cities = {'column': 'id_city', 'value': address['id_city']}
    _filter_to_counties = {'column': 'id_county', 'value': address['id_county']}
    _filter_to_states = {'column': 'id_state', 'value': address['id_state']}
    _filter_to_zips = {'column': 'id_zip', 'value': address['id_zip']}
    city = filter_data(cities_data, _filter_to_cities)[0]
    county = filter_data(counties_data, _filter_to_counties)[0]
    state = filter_data(states_data, _filter_to_states)[0]
    _zip = filter_data(zips_data, _filter_to_zips)[0]
    market['address']['street'] = address.get('street')
    market['address']['city'] = city.get('city')
    market['address']['county'] = county.get('county')
    market['address']['state'] = state.get('state')
    market['address']['zip'] = _zip.get('zip')
    return market


def get_categories(market: dict):
    market['categories'] = []
    categories_data = request("db/Categories.csv")
    markets_categories_data = request("db/MarketsCategories.csv")
    for item in markets_categories_data:
        if item['fmid'] == market['fmid']:
            for category in categories_data:
                if category['id_category'] == item['id_category']:
                    market['categories'].append(category['category'])
    return market


def get_payments(market: dict):
    market['payments'] = []
    payments_data = request("db/Payments.csv")
    markets_payments_data = request("db/MarketsPayments.csv")
    for item in markets_payments_data:
        if item['fmid'] == market['fmid']:
            for payment in payments_data:
                if payment['id_payment'] == item['id_payment']:
                    market['payments'].append(payment['payment'])
    return market


def make_show(args):
    if not check(args):
        return False
    market_result = {}
    fmid = args[0]
    markets_data = request("db/Markets.csv")
    for market in markets_data:
        if market['fmid'] == fmid:
            market_result = market
    if market_result:
        market = get_categories(market_result)
        market = get_payments(market_result)
        market = get_full_address(market_result)
        return market
    else:
        print("No market on this FMID")
        return False


if __name__ == "__main__":
    result = make_show(['1019938'])
    print(result)
