import sys
import time


from views.console.view import view
from controller.txt import BYE, GUIDE


COMMANDS = ('list', 'find', 'show', 'add_review', 'guide', 'exit')


def handler(cmd, args):
    if cmd not in COMMANDS:
        print('Wrong command!')
        time.sleep(2)
        sys.exit(1)
    elif cmd == 'exit':
        print(BYE)
        time.sleep(2)
        sys.exit()
    elif cmd == 'guide':
        print(GUIDE)
    else:
        view(cmd, args)
