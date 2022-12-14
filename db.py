from tools.read import read_farms
from tools.create import create_market_data, create_items_data, create_market_items_data
from tools.write import write


def create_db():
    data = read_farms("Export.csv")
    market_data = create_market_data(data)
    items_data = create_items_data(data)
    market_items_data = create_market_items_data(data, items_data)
    write("Market.csv", market_data)
    write("Items.csv", items_data,)
    write("MarketItems.csv", market_items_data)


if __name__ == "__main__":
    create_db()
    with open('Market.csv', 'r') as f:
        for row in f:
            data = row.strip().split(';')
            if len(data) > 29:
                print(data)