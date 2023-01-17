from model.mysql.connection import create_connection
from model.commands.list import get_data
from views.list import show_output


SORTES = ('fmid', 'marketname', 'rate')
REVERSE = {
    '+': True,
    '-': False,
    "": True
}


def check_params(param, reverse):
    if param in SORTES and reverse in REVERSE.keys():
        return True
    elif param not in SORTES:
        print('Wrong parameter')
    elif reverse not in REVERSE.keys():
        print("Wrong reverse")


def execute_list():
    param = input(
        "==> Enter sorting parameter ('fmid', 'marketname', 'rate'): "
    ).strip().lower()
    reverse = input(
        "==> Enter reverse ('+' increase, '-' decrease) or skip: "
    ).strip()
    if check_params(param, reverse) is True:
        status, db = create_connection("FarmMarkets")
        if status is True:
            cursor = db.cursor(dictionary=True, buffered=True)
            markets = get_data(cursor)
            print(markets)
            db.close()
            markets.sort(key=lambda x: x[param], reverse=REVERSE.get(reverse))
            show_output(markets)
        else:
            print(db)


if __name__ == "__main__":
    execute_list()
