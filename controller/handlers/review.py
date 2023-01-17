import re


from model.mysql.connection import create_connection
from model.commands.review import insert_user, get_user_by_email, get_market_id, insert_review


def check_email(email):
    if re.match("^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$", email):
        return True
    else:
        print("Invalid email")    


def execute_review():
    review = {}
    fmid = input("==> Enter market's fmid you want to give feedback: ")
    status, db = create_connection("FarmMarkets")
    if status is False:
        print(db)
    else:
        cursor = db.cursor(dictionary=True, buffered=True)
        market_id = get_market_id(cursor, fmid)
        if not market_id:
            print("No market was found at fmid №{}".format(fmid))
            db.close()
        else:
            review['Markets_idMarkets'] = market_id[0]['idMarkets']
            email = input("==> Enter your email: ").strip().lower()
            if not check_email(email):
                db.close()
            else:
                user_id = get_user_by_email(cursor, email)
                if not user_id:
                    print("You are new user! Please enter your personal")
                    user = {}
                    user['email'] = email
                    user['secondname'] = input("==> Enter your second name: ").strip().title()
                    user['firstname'] = input("==> Enter your name: ").strip().title()
                    insert_user(cursor, user)
                    db.commit()
                    user_id = get_user_by_email(cursor, email)
                review['Users_idUsers'] = user_id[0]['idUsers']
                flag = False
                while flag is False:
                    rate = input("Enter you rate from 1 to 5 point: ").strip()
                    try:
                        review['rate'] = int(rate)
                    except ValueError:
                        print("Wrong type of rate")
                    else:
                        flag = True
                review['review'] = input("Write about your experience (255 symb): ")
                insert_review(cursor, review)
                db.commit()
                print("Review added successfully")
                db.close()
