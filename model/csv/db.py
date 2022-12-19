import os


def create_markets_table():
    with open("db/Markets.csv", 'w') as f:
        fields = [
            'fmid', 'marketname', 'website', 'facebook', 'twitter',
            'youtube', 'othermedia', 'x', 'y',
            'location', 'updatetime']
        f.write(';'.join(fields) + '\n')


def create_addresses_table():
    with open("db/Addresses.csv", 'w') as f:
        fields = ['id_address', 'id_state', 'id_county', 'id_city', 'id_zip', 'street', 'fmid']
        f.write(';'.join(fields) + '\n')


def create_states_table():
    with open("db/States.csv", 'w') as f:
        fields = ['id_state', 'state']
        f.write(';'.join(fields) + '\n')


def create_counties_table():
    with open("db/Counties.csv", 'w') as f:
        fields = ['id_county', 'county']
        f.write(';'.join(fields) + '\n')


def create_cities_table():
    with open("db/Cities.csv", 'w') as f:
        fields = ['id_city', 'city']
        f.write(';'.join(fields) + '\n')


def create_zips_table():
    with open("db/Zips.csv", 'w') as f:
        fields = ['id_zip', 'zip']
        f.write(';'.join(fields) + '\n')


def create_categories_table():
    with open("db/Categories.csv", 'w') as f:
        fields = ['id_category', 'category']
        f.write(';'.join(fields) + '\n')


def create_payments_table():
    with open("db/Payments.csv", 'w') as f:
        fields = ['id_payment', 'payment']
        f.write(';'.join(fields) + '\n')


def create_markets_payments_table():
    with open("db/MarketsPayments.csv", 'w') as f:
        fields = ['fmid', 'id_payment']
        f.write(';'.join(fields) + '\n')


def create_markets_categories_table():
    with open("db/MarketsCategories.csv", 'w') as f:
        fields = ['fmid', 'id_category']
        f.write(';'.join(fields) + '\n')


def create_season1_table():
    with open('db/Season1.csv', 'w') as f:
        fields = ['fmid', 'date', 'time']
        f.write(';'.join(fields) + '\n')


def create_season2_table():
    with open('db/Season2.csv', 'w') as f:
        fields = ['fmid', 'date', 'time']
        f.write(';'.join(fields) + '\n')


def create_season3_table():
    with open('db/Season3.csv', 'w') as f:
        fields = ['fmid', 'date', 'time']
        f.write(';'.join(fields) + '\n')


def create_season4_table():
    with open('db/Season4.csv', 'w') as f:
        fields = ['fmid', 'date', 'time']
        f.write(';'.join(fields) + '\n')


def create_db():
    if not os.path.exists('db'):
        os.mkdir('db')
    create_markets_table()
    create_addresses_table()
    create_states_table()
    create_counties_table()
    create_cities_table()
    create_zips_table()
    create_categories_table()
    create_payments_table()
    create_markets_categories_table()
    create_markets_payments_table()
    create_season1_table()
    create_season2_table()
    create_season3_table()
    create_season4_table()


if __name__ == "__main__":
    create_db()
