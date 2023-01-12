from ETL.read import read_farms
from ETL.transform import transform
from ETL.load import load


from config import Config


def main():
    data = read_farms(Config.SOURCE_PATH)
    data_to_load = transform(data)
    load(data_to_load)


if __name__ == "__main__":
    main()
