def create_market_data(data, fields):
    result = []
    count = 1
    for row in data:
        market = {}
        market['id_market'] = count
        for field in fields:
            try:
                market[field] = row[field]
            except KeyError:
                print(field)
        result.append(market)
        count += 1
    return result


def create_items_data(fields):
    result = []
    count = 1
    for field in fields:
        item = {}
        item['id_item'] = count
        item['item'] = field
        result.append(item)
        count += 1
    return result


def create_market_items_data(data, market, items):
    result = []
    for index, row in enumerate(data):
        market_items = {}
        for item in items:
            try:
                if row[item['item']] == 'Y':
                    market_items['id_market'] = market[index]['id_market']
                    market_items['id_item'] = item['id_item']
            except KeyError:
                print(index, '\n', row, '\n', item)
        result.append(market_items)
    return result
