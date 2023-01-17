from model.mysql.connection import create_connection
from model.commands.find import get_data
from views.find import show_output


FIELDS = ('city', 'county', 'state')


def check(field):
    if field in FIELDS:
        return True
    else:
        print("Wrong searching field")


def execute_find():
    field = input(
        "==> Enter searching field (city, county, state): "
    ).strip().lower()
    if check(field) is True:
        value = input("==> Enter name of field: ").strip()
        if field == 'state':
            value = value.upper()
        else:
            value = value.swapcase()
        status, db = create_connection("FarmMarkets")
        if status is True:
            cursor = db.cursor(dictionary=True, buffered=True)
            markets = get_data(field, value, cursor)
            db.close()
            show_output(markets)


if __name__ == "__main__":
    execute_find()
