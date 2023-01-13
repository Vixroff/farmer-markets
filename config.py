import os


from dotenv import load_dotenv


basedir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    DB_USER = os.getenv('USERNAME')
    DB_PASSWORD = os.getenv('PASSWORD')
    HOST = '127.0.0.1'
    MARKETS_PATH = os.path.join(basedir, 'data/Export.csv')


if __name__ == "__main__":
    print(Config.SOURCE_PATH)
