from views.commands import list, find, show, review


def show_list(data):
    if data:
        for row in data:
            print("FMID:{fmid}, MARKETNAME: {marketname}, RATING: {rating}".format(**row))


def show_find(data):
    if data:
        for row in data:
            print("\n")
            print(f"Searching parametres: {row['mode']} - {row['value']}")
            for market in row['markets']:
                print(f"{market['fmid']} - {market['marketname']}")
            print("\n")


def show_show(data):
    if data:
        print(
            f"""
            FarmMarket №{data['fmid']}:
                "{data['marketname']}"

            Categories: 
                {', '.join(data.get('categories'))}
            Payments: 
                {', '.join(data.get('payments'))}

            Seasons of working: 
                Season 1 - {data['seasons'].get('season1')}
                Season 2 - {data['seasons'].get('season2')}
                Season 3 - {data['seasons'].get('season3')}
                Season 4 - {data['seasons'].get('season4')}

            Address: 
                street: {data['address'].get('street')}
                city: {data['address'].get('city')}
                county: {data['address'].get('county')}
                state: {data['address'].get('state')}
                zip code: {data['address'].get('zip')}
            
            Social:
                website: {data.get('website')}
                facebook: {data.get('facebook')}
                twitter: {data.get('twitter')}
                youtube: {data.get('youtube')}
            """
        )


def view(cmd, args):
    if cmd == 'list':
        result = list.make_list(args)
        show_list(result)     
    elif cmd == 'find':
        result = find.make_find(args)
        show_find(result)
    elif cmd == 'show':
        result = show.make_show(args)
        show_show(result)
    elif cmd == 'review':
        result = review.make_review(args)
        print(result)
