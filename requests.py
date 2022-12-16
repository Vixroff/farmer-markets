SORT_MODES = ['1', '2', '3', '']
FIND_MODES = ['1', '2', '3']



def requests_find(args):
    if len(args) % 2 != 0:
        print('Wrong type of input!')
        return False
    filters = []
    for i in range(0, len(args), 2):
        mode = args[i]
        value = args[i+1]
        if mode in FIND_MODES:
            _filter = (mode, value)
            filters.append(_filter)
        else:
            print("Wrong 'filter' argument")
            return False
    result = []
    for _filter in filters:
        mode = _filter[0]
        value = _filter[1]
        if mode == '1':
            city_id = None
            with open("db/Cities.csv", 'r') as f:
                f.readline()
                for row in f:
                    data = row.strip().split(';')
                    if value.lower() == data[1].lower():
                        city_id = data[0]
            if city_id is not None:
                markets = []
                with open("db/Addresses.csv", 'r') as f:
                    f.readline()
                    for row in f:
                        data = row.strip().split(';')
                        if city_id == data[3]:
                            markets.append(data[5])
                with open("db/Markets.csv", 'r') as f:
                    f.readline()
                    for row in f:
                        data = row.strip().split(';')
                        if data[0] in markets:
                            market = [data[0], data[1]]
                            result.append(market)
            else:
                result.append('No result for {} {}'.format(mode, value))
    return result            


if __name__ == "__main__":
    data = request_list('2')
    for market in data:
        print("marketname: {}".format(market[1]))