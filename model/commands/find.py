from model.mysql.connection import create_connection


QUERIES_TYPES = {
    'city': 'Cities',
    'state': 'States',
    'county': 'Counties'
}


def get_data(filter):
    column = filter['column']
    value = filter['value']
    table = QUERIES_TYPES.get(column)
    status, answer = create_connection("FarmMarkets")
    if status is True:
        query = f"""
        SELECT ma.fmid, ma.marketname
        FROM FarmMarkets.Markets as ma
            INNER JOIN FarmMarkets.Locations as lo
                ON ma.idMarkets = lo.Markets_idMarkets
            INNER JOIN FarmMarkets.{table} as ci
                ON lo.{table}_id{table} = ci.id{table}
        WHERE ci.{column} = '{value}'
        """
        db = answer
        cursor = db.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    else:
        print(answer)


if __name__ == "__main__":
    get_data({'column': 'city', 'value': 'New York'})
