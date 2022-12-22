import os


basedir = os.path.dirname(os.path.abspath(__file__))


class Config:
    SOURCE_DATA = os.path.join(basedir, 'Export.csv')
    MARKETS = os.path.join(basedir, 'db/Markets.csv')
    ADDRESSES = os.path.join(basedir, 'db/Addresses.csv')
    CATEGORIES = os.path.join(basedir, 'db/Categories.csv')
    CITIES = os.path.join(basedir, 'db/Cities.csv')
    COUNTIES = os.path.join(basedir, 'db/Counties.csv')
    MARKETS_CATEGORIES = os.path.join(basedir, 'db/MarketsCategories.csv')
    MARKETS_PAYMENTS = os.path.join(basedir, 'db/MarketsPayments.csv')
    PAYMENTS = os.path.join(basedir, 'db/Payments.csv')
    SEASON1 = os.path.join(basedir, 'db/Season1.csv')
    SEASON2 = os.path.join(basedir, 'db/Season2.csv')
    SEASON3 = os.path.join(basedir, 'db/Season3.csv')
    SEASON4 = os.path.join(basedir, 'db/Season4.csv')
    STATES = os.path.join(basedir, 'db/States.csv')
    ZIPS = os.path.join(basedir, 'db/Zips.csv')
    USERS = os.path.join(basedir, 'db/Users.csv')
    REVIEWS = os.path.join(basedir, 'db/Reviews.csv')


if __name__ == "__main__":
    print(Config.SOURCE_DATA)
    print(Config.REVIEWS)