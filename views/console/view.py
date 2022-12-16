from views.console.cmd_list import cmd_list


def view(cmd, args):
    if cmd == 'list':
        result = cmd_list(args)
        if result:
            for item in result:
                print(
                    "FMID:{fmid}, MARKETNAME: {marketname}, RATING: {rating}".format(**item)
                )
