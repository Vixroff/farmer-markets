from model.commands.list import get_data
from views.commands.list import show_output


SORTES = ('fmid', 'marketname', 'rate')
REVERSE = ('False', 'True')


def check_params(param, reverse):
    if param in SORTES and reverse in REVERSE:
        return True
    elif param not in SORTES:
        print('Wrong parameter')
    elif reverse not in REVERSE:
        print("Wrong reverse")


def execute_list():
    param = input(
        "==> Enter sorting parameter ('fmid', 'marketname', 'rate'): "
    ).strip().lower()
    reverse = input(
        "==> Enter reverse ('True' increase, 'False' decrease): "
    ).strip().title()
    if check_params(param, reverse) is True:
        markets = get_data()
        markets.sort(key=lambda x: x[param], reverse=bool(reverse))
        show_output(markets)


if __name__ == "__main__":
    execute_list()
