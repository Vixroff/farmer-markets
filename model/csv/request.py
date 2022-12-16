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


def get_filtered_data(path: str, _filter: dict) -> list:
    data = request(path)
    filtered_data = []
    for row in data:
        if _filter['value'] == row[_filter['column']]:
            filtered_data.append(row)
        else:
            continue
    return filtered_data
