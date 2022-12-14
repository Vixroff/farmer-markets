def check(data):
    new_data = []
    new_value = []
    for value in data:
        if '""' in value:
            value = value.replace('""', '"')
        if value.startswith('"') and value != '"':
            new_value.append(value)
        elif value.endswith('"') or value == '"':
            new_value.append(value)
            new_data.append(','.join(new_value))
            new_value = []
        elif new_value:
            new_value.append(value)
        else:
            new_data.append(value)
    return new_data      


def read_farms(path):
    with open(path, 'r') as f:
        result = []
        for row in f:
            data = row.strip().split(',')
            if len(data) > 59:
                data = check(data)
            result.append(data)                        
        return result
