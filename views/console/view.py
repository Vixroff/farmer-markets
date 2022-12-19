from views.commands import list, find, show


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
        print(data)


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
