import time


from ETL.read import read_farms


def get_categories_data(data):
    result = []
    id_category = 1
    for value in data[28:58]:
        category_data = {}
        category_data['id_category'] = id_category
        category_data['category'] = value
        result.append(category_data)
        id_category += 1
    return result


def get_payments_data(data):
    result = []
    id_payment = 1
    for value in data[23:28]:
        payment_data = {}
        payment_data['id_payment'] = id_payment
        payment_data['payment'] = value
        result.append(payment_data)
        id_payment += 1
    return result


def get_states_data(data):
    result = []
    states = set()
    for row in data[1:]:
        states.add(row['state'])
    id_state = 1
    for state in states:
        if state:
            state_data = {}
            state_data['id_state'] = id_state
            state_data['state'] = state
            result.append(state_data)
            id_state += 1
        else:
            continue
    return result


def get_counties_data(data):
    result = []
    counties = set()
    for row in data[1:]:
        counties.add(row['county'])
    id_county = 1
    for county in counties:
        if county:
            county_data = {}
            county_data['id_county'] = id_county
            county_data['county'] = county
            result.append(county_data)
            id_county += 1
        else:
            continue
    return result


def get_cities_data(data):
    result = []
    cities = set()
    for row in data[1:]:
        cities.add(row['city'])
    id_city = 1
    for city in cities:
        if city:
            city_data = {}
            city_data['id_city'] = id_city
            city_data['city'] = city
            result.append(city_data)
            id_city += 1
        else:
            continue
    return result


def get_zips_data(data):
    result = []
    zips = set()
    for row in data[1:]:
        zips.add(row['zip'])
    id_zip = 1
    for zip in zips:
        if zip:
            zip_data = {}
            zip_data['id_zip'] = id_zip
            zip_data['zip'] = zip
            result.append(zip_data)
            id_zip += 1
        else:
            continue
    return result
        

def get_address_data(data, states, counties, cities):
    result = []
    id_address = 1
    for row in data[1:]:
        address_data = {}
        address_data['id_address'] = id_address
        address_data['fmid'] = row['fmid']
        address_data['street'] = row['street']
        for state in states:
            if state.get('state') == row['state']:
                address_data['id_state'] = state['id_state']
                break
            else:
                continue
        if not address_data.get('id_state'):
            address_data['id_state'] = None
        for county in counties:
            if county.get('county') == row['county']:
                address_data['id_county'] = county['id_county']
                break
            else:
                continue
        if not address_data.get('county'):
            address_data['id_county'] = None
        for city in cities:
            if city.get('city') == row['city']:
                address_data['id_city'] = city['id_city']
                break
            else:
                continue
        if not address_data.get('id_city'):
            address_data['id_city'] = None
        result.append(address_data)
        id_address += 1
    return result


def get_markets_data(data, zips):
    result = []
    for row in data[1:]:
        market_data = {}
        market_data['fmid'] = row['fmid']
        market_data['marketname'] = row['marketname']
        market_data['website'] = row['website']
        market_data['facebook'] = row['facebook']
        market_data['twitter'] = row['twitter']
        market_data['youtube'] = row['youtube']
        market_data['othermedia'] = row['othermedia']
        market_data['x'] = row['x']
        market_data['y'] = row['y']
        market_data['location'] = row['location']
        market_data['updatetime'] = row['updatetime']
        for zip in zips:
            if zip.get('zip') == row['zip']:
                market_data['id_zip'] = zip['id_zip']
                break
            else:
                continue
        if not market_data.get('id_zip'):
            market_data['id_zip'] = None
        result.append(market_data)
    return result


def get_markets_payments_data(data, payments):
    result = []
    for row in data[1:]:
        for payment in payments:
            markets_payments_data = {}
            key = payment.get('payment')
            if row.get(key) == 'Y':
                markets_payments_data['fmid'] = row.get('fmid')
                markets_payments_data['id_payment'] = payment.get('id_payment')
                result.append(markets_payments_data)
            else:
                continue
    return result


def get_markets_categories_data(data, categories):
    result = []
    for row in data[1:]:
        for category in categories:
            markets_categories_data = {}
            key = category.get('category')
            if row.get(key) == 'Y':
                markets_categories_data['fmid'] = row.get('fmid')
                markets_categories_data['id_category'] = category.get('id_category')
                result.append(markets_categories_data)
            else:
                continue
    return result


def get_season1_data(data):
    result = []
    for row in data[1:]:
        season1_data = {}
        if row.get('season1date'):
            season1_data['fmid'] = row['fmid']
            season1_data['date'] = row['season1date']
            season1_data['time'] = row['season1time'].replace(';', '/')
            result.append(season1_data)
    return result


def get_season2_data(data):
    result = []
    for row in data[1:]:
        season2_data = {}
        if row.get('season2date'):
            season2_data['fmid'] = row['fmid']
            season2_data['date'] = row['season2date']
            season2_data['time'] = row['season2time'].replace(';', '/')
            result.append(season2_data)
    return result


def get_season3_data(data):
    result = []
    for row in data[1:]:
        season3_data = {}
        if row.get('season3date'):
            season3_data['fmid'] = row['fmid']
            season3_data['date'] = row['season3date']
            season3_data['time'] = row['season3time'].replace(';', '/')
            result.append(season3_data)
    return result


def get_season4_data(data):
    result = []
    for row in data[1:]:
        season4_data = {}
        if row.get('season4date') != '':
            season4_data['fmid'] = row['fmid']
            season4_data['date'] = row['season4date']
            season4_data['time'] = row['season4time'].replace(';', '/')
            result.append(season4_data)
    return result


def transform():
    start = time.time()
    data = read_farms("Export.csv")
    payments = get_payments_data(data[0])
    categories = get_categories_data(data[0])
    states = get_states_data(data)
    counties = get_counties_data(data)
    cities = get_cities_data(data)
    zips = get_zips_data(data)
    addresses = get_address_data(data, states, counties, cities)
    markets = get_markets_data(data, zips)
    markets_payments = get_markets_payments_data(data, payments)
    markets_categories = get_markets_categories_data(data, categories)
    season1 = get_season1_data(data)
    season2 = get_season2_data(data)
    season3 = get_season3_data(data)
    season4 = get_season4_data(data)
    finish = time.time()
    print(finish - start)
    return{
        'payments': payments,
        'categories': categories,
        'states': states,
        'counties': counties,
        'cities': cities,
        'zips': zips,
        'addresses': addresses,
        'markets': markets,
        'markets_payments': markets_payments,
        'markets_categories': markets_categories,
        'season1': season1,
        'season2': season2,
        'season3': season3,
        'season4': season4,
    }


if __name__ == "__main__":
    tranformed_data = transform()
    print(tranformed_data['season4'][5])
