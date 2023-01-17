QUERIES_TYPES = {
    'city': 'Cities',
    'state': 'States',
    'county': 'Counties'
}


def get_data(field, value, cursor):
    table = QUERIES_TYPES.get(field)
    query = f"""
    SELECT fmid, marketname
    FROM FarmMarkets.Markets
        INNER JOIN FarmMarkets.Locations
            ON idMarkets = Markets_idMarkets
        INNER JOIN FarmMarkets.{table}
            ON {table}_id{table} = id{table}
    WHERE {field} = '{value}'
    """
    cursor.execute(query)
    result = cursor.fetchall()
    return result


if __name__ == "__main__":
    result = get_data('city', 'New York')
    print(result)
    
