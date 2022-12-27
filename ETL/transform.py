from datetime import datetime


from ETL.read import read_farms
from config import Config


def get_states_data(data):
    result = []
    states = set()
    for row in data:
        states.add(row['state'])
    id_state = 1
    for state in states:
        if state:
            state_data = {}
            state_data['idStates'] = id_state
            state_data['state'] = state
            result.append(state_data)
            id_state += 1
    return result


def get_counties_data(data):
    result = []
    counties = set()
    for row in data:
        counties.add(row['county'])
    id_county = 1
    for county in counties:
        if county:
            county_data = {}
            county_data['idCounties'] = id_county
            county_data['county'] = county
            result.append(county_data)
            id_county += 1
    return result


def get_cities_data(data):
    result = []
    cities = set()
    for row in data:
        cities.add(row['city'])
    id_city = 1
    for city in cities:
        if city:
            city_data = {}
            city_data['idCities'] = id_city
            city_data['city'] = city
            result.append(city_data)
            id_city += 1
    return result


def get_zips_data(data):
    result = []
    zips = set()
    for row in data:
        zips.add(row['zip'])
    id_zip = 1
    for zip in zips:
        if zip:
            zip_data = {}
            zip_data['idZips'] = id_zip
            zip_data['zip'] = zip
            result.append(zip_data)
            id_zip += 1
    return result


def get_location_data(data, states, counties, cities, zips):
    result = []
    id_market = 1
    for row in data:
        location_data = {}
        location_data['idLocations'] = id_market
        location_data['Markets_idMarkets'] = id_market
        location_data['street'] = row['street']
        location_data['x'] = row['x']
        location_data['y'] = row['y']
        location_data['location'] = row['location']
        for state in states:
            if row['state'] == state.get('state'):
                location_data['States_idStates'] = state['idStates']
                break
        for county in counties:
            if row['county'] == county.get('county'):
                location_data['Counties_idCounties'] = county['idCounties']
                break
        for city in cities:
            if row['city'] == city.get('city'):
                location_data['Cities_idCities'] = city['idCities']
                break
        for zip in zips:
            if row['zip'] == zip.get('zip'):
                location_data['Zips_idZips'] = zip['idZips']
                break
        result.append(location_data)
        id_market += 1
    return result


def get_markets_data(data):
    result = []
    id_market = 1
    for row in data:
        market_data = {}
        market_data['idMarkets'] = id_market
        market_data['fmid'] = row['fmid']
        market_data['marketname'] = row['marketname']
        time = datetime.strftime(
            datetime.strptime(row['updatetime'], '%m/%d/%Y %I:%M:%S %p'), '%Y-%m-%d %H:%M:%S' 
        )
        market_data['updatetime'] = time
        id_market += 1
        result.append(market_data)
    return result


def get_categories_data(data):
    result = []
    id_category = 1
    for value in data[28:58]:
        category_data = {}
        category_data['idCategories'] = id_category
        category_data['category'] = value
        result.append(category_data)
        id_category += 1
    return result


def get_payments_data(data):
    result = []
    id_payment = 1
    for value in data[23:28]:
        payment_data = {}
        payment_data['idPayments'] = id_payment
        payment_data['payment'] = value
        result.append(payment_data)
        id_payment += 1
    return result


def get_markets_payments_data(data, payments):
    result = []
    market_index = 1
    for row in data:
        for payment in payments:
            markets_payments_data = {}
            key = payment.get('payment')
            if row[key] == 'Y':
                markets_payments_data['Markets_idMarkets'] = market_index
                markets_payments_data['Payments_idPayments'] = payment['idPayments']
                result.append(markets_payments_data)
        market_index += 1
    return result


def get_markets_categories_data(data, categories):
    result = []
    market_index = 1
    for row in data:
        for category in categories:
            markets_categories_data = {}
            key = category.get('category')
            if row[key] == 'Y':
                markets_categories_data['Markets_idMarkets'] = market_index
                markets_categories_data['Categories_idCategories'] = category['idCategories']
                result.append(markets_categories_data)
        market_index += 1
    return result


def get_seasons_data(data):
    result = []
    id_market = 1
    for row in data:
        season = {}
        season['Markets_idMarkets'] = id_market
        season['season1'] = row['season1date']
        season['season1_time'] = row['season1time']
        season['season2'] = row['season2date']
        season['season2_time'] = row['season2time']
        season['season3'] = row['season3date']
        season['season3_time'] = row['season3time']
        season['season4'] = row['season4date']
        season['season4_time'] = row['season4time']
        result.append(season)
        id_market += 1
    return result


def get_media_data(data):
    result = []
    id_market = 1
    for row in data:
        media = {}
        media['website'] = row['website']
        media['facebook'] = row['facebook']
        media['twitter'] = row['twitter']
        media['youtube'] = row['youtube']
        media['othermedia'] = row['othermedia']
        media['Markets_idMarkets'] = id_market
        result.append(media)
        id_market += 1
    return result


def transform(data):
    fields = data[0]
    content = data[1:]
    markets = get_markets_data(content)
    media = get_media_data(content)
    seasons = get_seasons_data(content)
    payments = get_payments_data(fields)
    markets_payments = get_markets_payments_data(content, payments)
    categories = get_categories_data(fields)
    markets_categories = get_markets_categories_data(content, categories)
    states = get_states_data(content)
    counties = get_counties_data(content)
    cities = get_cities_data(content)
    zips = get_zips_data(content)
    locations = get_location_data(content, states, counties, cities, zips)
    return{
        'Payments': payments,
        'Categories': categories,
        'States': states,
        'Counties': counties,
        'Cities': cities,
        'Zips': zips,
        'Locations': locations,
        'Markets': markets,
        'Markets_has_Payments': markets_payments,
        'Markets_has_Categories': markets_categories,
        'Seasons': seasons,
        'Media': media
        }


if __name__ == "__main__":
    data = read_farms(Config.SOURCE_PATH)
    transformed = transform(data)

    for row in transformed['Seasons']:
        if len(row['season1_time']) > 100:
            print(len(row['season1_time']))

    print(transformed['Markets'])

    count = 1
    for data in transformed['Markets']:
        if 'Alexandria Farmers Market' in data['marketname']:
            print(data, count)
        count += 1

    for row in transformed['Locations']:
        if 30 == row['Markets_idMarkets']:
            print(row)
        if 31 == row['Markets_idMarkets']:
            print(row)

    for row in transformed["Locations"]:
        if not row.get('States_idStates'):
            print(row)

    for row in transformed["Markets"]:
        if row['fmid'] == '1018261':
            print(row)
            print('\n')