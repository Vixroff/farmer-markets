from model.mysql.connection import create_connection


def markets_exists(cursor, fmid):
    query = "SELECT * FROM Markets WHERE fmid = %s"
    cursor.execute(query, [fmid])
    market = cursor.fetchall()
    if market:
        return True


def get_market_id(cursor, fmid):
    query = "SELECT idMarkets FROM Markets WHERE fmid = %s;"
    cursor.execute(query, [fmid])
    market_id = cursor.fetchall()
    return market_id


def insert_user(cursor, user: dict):
    query = """
    INSERT INTO Users (firstname, secondname, email)
    VALUES (%s, %s, %s);
    """
    values = (user['firstname'], user['secondname'], user['email'])
    cursor.execute(query, values)


def get_user_by_email(cursor, email):
    query = """
    SELECT idUsers
    FROM Users
    WHERE email = '{}';
    """.format(email)
    cursor.execute(query)
    user = cursor.fetchall()
    return user


def insert_review(cursor, review: dict):
    query = """
    INSERT INTO Reviews (Markets_idMarkets, Users_idUsers, rate, review)
    VALUES (%s, %s, %s, %s)
    """
    values = (review['Markets_idMarkets'], review['Users_idUsers'], review['rate'], review['review'])
    cursor.execute(query, values)


if __name__ == "__main__":
    markets_exists('1004950')
