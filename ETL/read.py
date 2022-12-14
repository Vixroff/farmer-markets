def read_farms(path):
    with open(path, 'r') as f:
        result = []
        keys = f.readline().lower().strip().split(',')
        result.append(keys)
        for row in f:
            data = {}
            values = format(row)
            for index, key in enumerate(keys):
                data[key] = values[index]
            result.append(data)                        
        return result


def format(data):
    sep_data = data.strip().split(',')
    formatted_data = []
    formatted_value = []
    for value in sep_data:
        value = value.replace("\"\"", "\"")
        if value.startswith("\"") and value != "\"":
            formatted_value.append(value[1:])
        elif value.endswith("\"") or value == "\"":
            formatted_value.append(value[:-1])
            formatted_data.append(','.join(formatted_value))
            formatted_value = []
        elif formatted_value:
            formatted_value.append(value)
        else:
            formatted_data.append(value)
    return formatted_data
    

if __name__ == "__main__":
    data = read_farms("Export.csv")
    for row in data:
        for value in row.values():
            if "\"" in value:
                print(row)
