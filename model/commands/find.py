from model.mysql.connection import create_connection


QUERIES_TYPES = {
    'city': 'Cities',
    'state': 'States',
    'county': 'Counties'
}


def get_data(field, value):
    result = []
    table = QUERIES_TYPES.get(field)
    status, answer = create_connection("FarmMarkets")
    if status is True:
        query = f"""
        SELECT fmid, marketname
        FROM FarmMarkets.Markets
            INNER JOIN FarmMarkets.Locations
                ON idMarkets = Markets_idMarkets
            INNER JOIN FarmMarkets.{table}
                ON {table}_id{table} = id{table}
        WHERE {field} = '{value}'
        """
        db = answer
        cursor = db.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
    else:
        print(answer)
    return result


if __name__ == "__main__":
    result = get_data('city', 'New York')
    print(result)
    
