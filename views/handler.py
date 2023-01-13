import sys
import time


from controller.txt import BYE, GUIDE
from views.commands.list import execute_list
from views.commands.find import execute_find

COMMANDS = ('list', 'find', 'show', 'review', 'guide', 'exit')


def handler(cmd, args):
    if cmd not in COMMANDS:
        print('Wrong command!')
        time.sleep(1)
    elif cmd == 'exit':
        print(BYE)
        time.sleep(1)
        sys.exit()
    elif cmd == 'guide':
        print(GUIDE)
    elif cmd == 'list':
        execute_list(args)
    elif cmd == 'find':
        execute_find(args)
    else:
        pass
