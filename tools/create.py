from tools.read import read_farms


def create_market_data(data):
    result = []
    for row in data:
        result.append(row[:28])
    return result


def create_items_data(data):
    result = [['id_item', 'item']]
    fields = data[0]
    count = 1
    for field in fields[28:58]:
        result.append([str(count), field])
        count += 1
    return result


def create_market_items_data(data, items):
    result = [['FMID', 'id_item']]
    for row in data:
        count = 1
        for value in row[28:58]:
            if value == "Y":
                result.append([row[0], items[count][0]])
            count += 1
    return result


if __name__ == "__main__":
    pass
