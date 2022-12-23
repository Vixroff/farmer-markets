from views.commands import list, find, show, review


def view(cmd, args):
    if cmd == 'list':
        list.list_console(args)    
    elif cmd == 'find':
        find.find_console(args)
    elif cmd == 'show':
        show.show_console(args)
    elif cmd == 'review':
        review.review_console(args)
