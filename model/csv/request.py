def request(path: str) -> list:
    result = []
    with open(path, 'r') as f:
        fields = f.readline().strip().split(';')
        for row in f:
            item = {}
            data = row.strip().split(';')
            for index, field in enumerate(fields):
                item[field] = data[index]
            result.append(item)
    return result


def filter_data(data: list, _filter: dict) -> list:
    filtered_data = []
    for row in data:
        if _filter['value'] == row[_filter['column']]:
            filtered_data.append(row)
        else:
            continue
    return filtered_data


def write(data, path):
    with open(path, 'r+') as f:
        fields = f.readline().strip().split(';')
        for row in data:
            to_write = []
            for field in fields:
                try:
                    to_write.append(str(row[field]))
                except KeyError as e:
                    print(e, row)
            f.write(';'.join(to_write) + '\n')
