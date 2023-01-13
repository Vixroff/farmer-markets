from model.commands.find import get_data
from views.commands.find import show_output


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
        markets = get_data(field, value)
        show_output(markets)


if __name__ == "__main__":
    execute_find()
