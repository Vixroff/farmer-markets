import mysql.connector
from mysql.connector import errorcode


from config import Config


def create_connection(database=None):
    try:
        db = mysql.connector.connect(
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            host=Config.HOST,
            database=database)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return False, "Something is going wrong with your user name or password"
        else:
            return False, err
    else:
        return True, db
