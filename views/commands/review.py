from config import Config


from model.csv.request import request


def check(args):
    if not args:
        return False, "No FMID entered"
    if len(args) != 1 or len(args[0]) != 7:
        return False, "Please, enter your FMID index correctly!"
    markets_data = request(Config.MARKETS)
    for row in markets_data:
        if row['fmid'] == args[0]:
            return True, "Args is valid"
    return False, "No Market on this FMID"


def get_args(args):
    return args[0]


def make_review(fmid):
    rate_output = False
    while rate_output == False:
        rate = input("Enter your rate [1-5] for this market: ")
        if rate in ['1', '2', '3', '4', '5']:
            rate_output = True
        else:
            print("Enter your rate correctly ([1-5])")
    review = input("Write something about your experience in the market: ")
    firstname = input("Enter your firstname: ").strip().lower()
    lastname = input("Enter your lastname: ").strip().lower()
    users_data = request(Config.USERS)
    user_exists = False
    if users_data:
        for row in users_data:
            id_user = row['id_user']
            if lastname == row['lastname'] and firstname == row['firstname']:
                user_exists = True
                print('User is exists')
                break
        else:
            id_user = str(int(id_user) + 1)
    else:
        id_user = '1'
    if user_exists is False:
        with open(Config.USERS, 'a') as f:
            user = [id_user, firstname, lastname]
            f.write(';'.join(user) + '\n')
            print('New User added to db')
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
        print("Review was added")
    

def review_console(args):
    arguments_valudation = check(args)
    status = arguments_valudation[0]
    answer = arguments_valudation[1]
    if status is False:
        print(answer)
    else:
        fmid = get_args(args)
        make_review(fmid)
        

if __name__ == "__main__":
    make_review(['1018261'])
