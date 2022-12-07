from read import read, get_fields


def create_market_db(data, fields):
    result = []
    count = 1
    for row in data:
        market = {}
        market['id_market'] = count
        for field in fields:
            market[field] = row[field]
        result.append(market)
        count += 1
    return result


def create_items_db(fields):
    result = []
    count = 1
    for field in fields:
        item = {}
        item['id_item'] = count
        item['item'] = field
        result.append(item)
        count += 1
    return result


def create_market_items_db(data, market, items):
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


if __name__ == "__main__":
    data = read("Export.csv")

    fields = get_fields("Export.csv")
    fields_market = fields[:28]
    fields_items = fields[28:58]

    market_data = create_market_db(data, fields_market)
    items_data = create_items_db(fields_items)
    market_items_data = create_market_items_db(data, market_data, items_data)
    print(market_items_data)
