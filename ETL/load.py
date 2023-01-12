from model.mysql.connection import create_connection


DB = {
    'queue': [
        'Markets', 'States', 'Zips', 'Counties',
        'Cities', 'Categories', 'Payments', 'Locations',
        'Media', 'Seasons', 'Markets_has_Categories', 'Markets_has_Payments'
    ],
    'States': ['idStates', 'state'],
    'Zips': ['idZips', 'zip'],
    'Counties': ['idCounties', 'county'],
    'Cities': ['idCities', 'city'],
    'Categories': ['idCategories', 'category'],
    'Payments': ['idPayments', 'payment'],
    'Seasons': [
        'Markets_idMarkets', 'season1', 'season1_time',
        'season2', 'season2_time', 'season3',
        'season3_time', 'season4', 'season4_time'
    ],
    'Locations': [
        'idLocations', 'street', 'x', 'y',
        'location', 'States_idStates', 'Cities_idCities',
        'Counties_idCounties', 'Zips_idZips', 'Markets_idMarkets'
    ],
    'Markets': [
        'idMarkets', 'marketname', 'updatetime', 'fmid'
    ],
    'Markets_has_Categories': ['Markets_idMarkets', 'Categories_idCategories'],
    'Markets_has_Payments': ['Markets_idMarkets', 'Payments_idPayments'],
    'Media': ['Markets_idMarkets', 'youtube', 'facebook', 'website', 'othermedia']
}


def prepare_data(data, fields):
    result = []
    for row in data:
        prepared_data = []
        for field in fields:
            value = row.get(field)
            prepared_data.append(value)
        result.append(tuple(prepared_data))
    return result


def load(data):
    status, answer = create_connection("FarmMarkets")
    if status is True:
        db = answer
        cursor = db.cursor()
        for table in DB['queue']:
            fields = DB.get(table)
            content = prepare_data(data.get(table), fields)
            query = f"""
            INSERT INTO {table} ({', '.join(fields)})
            VALUES ({', '.join(['%s'] * len(fields))})
            """
            cursor.executemany(query, content)
        db.commit()
        db.close()
        print("Data was uploaded successfully")
    else:
        print(answer)


def main():
    load()


if __name__ == "__main__":
    main()
