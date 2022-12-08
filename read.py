def format_data(data):
    new_data = []
    new_value = []
    for value in data:
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


def read(path):
    with open(path, 'r') as f:
        result = []
        fields = f.readline().strip().split(',')
        for row in f:
            new_data = {}
            data = row.strip().split(',')
            if len(data) > 59:
                data = format_data(data)
            for i in range(len(data)):
                new_data[fields[i]] = data[i]
            result.append(new_data)                        
        return result
             

if __name__ == "__main__":
    data = read("Export.csv")