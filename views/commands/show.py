from config import Config


from model.csv.request import request, filter_data


def check(args):
    if not args:
        return False, "No FMID entered"
    if len(args) != 1 or len(args[0]) != 7:
        return False, "Please, enter your FMID index correctly!"
    markets_data = request(Config.MARKETS)
    for row in markets_data:
        if row['fmid'] == args[0]:
            return True, "Args are valid"
    return False, "No Market on this FMID"


def get_fmid(args):
    return args[0]


def get_full_address(market: dict):
    market['address'] = {}
    addresses_data = request(Config.ADDRESSES)
    cities_data = request(Config.CITIES)
    counties_data = request(Config.COUNTIES)
    states_data = request(Config.STATES)
    zips_data = request(Config.ZIPS)
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
    categories_data = request(Config.CATEGORIES)
    markets_categories_data = request(Config.MARKETS_CATEGORIES)
    for item in markets_categories_data:
        if item['fmid'] == market['fmid']:
            for category in categories_data:
                if category['id_category'] == item['id_category']:
                    market['categories'].append(category['category'])
    return market


def get_payments(market: dict):
    market['payments'] = []
    payments_data = request(Config.PAYMENTS)
    markets_payments_data = request(Config.MARKETS_PAYMENTS)
    for item in markets_payments_data:
        if item['fmid'] == market['fmid']:
            for payment in payments_data:
                if payment['id_payment'] == item['id_payment']:
                    market['payments'].append(payment['payment'])
    return market


def get_seasons(market: dict):
    market['seasons'] = {}
    season1_data = request(Config.SEASON1)
    season2_data = request(Config.SEASON2)
    season3_data = request(Config.SEASON3)
    season4_data = request(Config.SEASON4)
    filter_to_season = {'column': 'fmid', 'value': market['fmid']}
    season1 = filter_data(season1_data, filter_to_season)
    season2 = filter_data(season2_data, filter_to_season)
    season3 = filter_data(season3_data, filter_to_season)
    season4 = filter_data(season4_data, filter_to_season)
    if season1:
        market['seasons']['season1'] = [season1[0].get('date'), season1[0].get('time')]
    if season2:
        market['seasons']['season2'] = [season2[0].get('date'), season2[0].get('time')]
    if season3:
        market['seasons']['season3'] = [season3[0].get('date'), season3[0].get('time')]
    if season4:
        market['seasons']['season4'] = [season4[0].get('date'), season4[0].get('time')]
    return market


def execute_show(fmid):
    market = {}
    markets_data = request(Config.MARKETS)
    for row in markets_data:
        if row['fmid'] == fmid:
            market = row
            break
    market = get_categories(market)
    market = get_payments(market)
    market = get_full_address(market)
    market = get_seasons(market)
    return market


def show_output(data):
    print(
        f"""
        FarmMarket №{data['fmid']}:
            "{data['marketname']}"

        Categories: 
            {', '.join(data.get('categories'))}
        Payments: 
            {', '.join(data.get('payments'))}

        Seasons of working: 
            Season 1 - {data['seasons'].get('season1')}
            Season 2 - {data['seasons'].get('season2')}
            Season 3 - {data['seasons'].get('season3')}
            Season 4 - {data['seasons'].get('season4')}

        Address: 
            street: {data['address'].get('street')}
            city: {data['address'].get('city')}
            county: {data['address'].get('county')}
            state: {data['address'].get('state')}
            zip code: {data['address'].get('zip')}
        
        Social:
            website: {data.get('website')}
            facebook: {data.get('facebook')}
            twitter: {data.get('twitter')}
            youtube: {data.get('youtube')}
        """
    )


def show_console(args):
    arguments_validation = check(args)
    status = arguments_validation[0]
    answer = arguments_validation[1]
    if status is False:
        print(answer)
    else:
        fmid = get_fmid(args)
        result = execute_show(fmid)
        show_output(result)


if __name__ == "__main__":
    show_console(['1111111'])
