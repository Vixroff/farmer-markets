import sys
import time


from controller.blocks import GREETINGS, GUIDE 


COMMANDS = ['list', 'find', 'show', 'add_review', 'guide', 'exit']


def cmd_handler(cmd):
    commands_list = cmd.split(' ')
    command = commands_list[0]
    if command not in COMMANDS:
        print('Wrong command')
    elif command == 'exit':
        print('Execute EXIT')
        time.sleep(2)
        sys.exit(1)
    elif command == 'guide':
        print(GUIDE)
    elif command == 'list':
        print('Do list func')
    elif command == 'find':
        print('Do find func')
    elif command == 'show':
        print('Do show func')
    elif command == 'add_review':
        print('Do add_review')


def main():
    print(GREETINGS)
    while True:
        cmd = input('==> Enter a command: ')
        cmd_handler(cmd)


if __name__ == "__main__":
    main()
