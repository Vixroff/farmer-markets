from config import Config


from model.csv.request import request


def check(args):
    if not args:
        print("No FMID entered")
        return False
    if len(args) != 1 or len(args[0]) != 7:
        print("Please, enter your FMID index correctly!")
        return False
    markets_data = request(Config.MARKETS)
    for row in markets_data:
        if row['fmid'] == args[0]:
            return True
    print("No Market on this FMID")
    return False


def get_args(args):
    return args[0]


def make_review(args):
    if not check(args):
        return 'Process failed'
    fmid = get_args(args)
    rate_output = False
    while rate_output == False:
        rate = input("Enter your rate [1-5] for this market: ")
        if rate in ['1', '2', '3', '4', '5']:
            rate_output = True
    review = input("Write something about your experience in the market: ")
    firstname = input("Enter your firstname: ").strip().lower()
    lastname = input("Enter your lastname: ").strip().lower()
    users_data = request(Config.USERS)
    user_exists = False
    if users_data:
        for row in users_data:
            id_user = row['id_user']
            if lastname == row['lastname'] and firstname == row['lastname']:
                user_exists = True
                break
        else:
            id_user = str(int(id_user) + 1)
    else:
        id_user = '1'
    if not user_exists:
        with open(Config.USERS, 'a') as f:
            user = [id_user, firstname, lastname]
            f.write(';'.join(user) + '\n')
    reviews_data = request(Config.REVIEWS)
    if reviews_data:
        for row in reviews_data:
            id_review = row['id_review']
        id_review = str(int(id_review) + 1)
    else:
        id_review = '1'
    with open(Config.REVIEWS, 'a') as f:
        review = [id_review, id_user, fmid, rate, review]
        f.write(';'.join(review) + '\n')
    return 'Review added'
    

if __name__ == "__main__":
    make_review(['1018261'])
