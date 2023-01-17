from controller.handlers.exit import execute_exit
from controller.handlers.guide import execute_guide
from controller.handlers.list import execute_list
from controller.handlers.find import execute_find
from controller.handlers.review import execute_review


COMMANDS = ('list', 'find', 'show', 'review', 'guide', 'exit')


def handler(cmd):
    if cmd not in COMMANDS:
        print('Wrong command!')
    elif cmd == 'exit':
        execute_exit()
    elif cmd == 'guide':
        execute_guide()
    elif cmd == 'list':
        execute_list()
    elif cmd == 'find':
        execute_find()
    elif cmd == 'review':
        execute_review()
