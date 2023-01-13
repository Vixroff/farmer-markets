from controller.handler import handler


from controller.txt import GREETINGS


def get_command(input):
    items = input.split(' ')
    command = items[0]
    if len(items) > 1:
        args = items[1:]
    else:
        args = None
    return command, args


def start():
    print(GREETINGS)
    while True:
        users_input = input('==> Enter a command: ')
        command, args = get_command(users_input)
        handler(command, args)


if __name__ == "__main__":
    start()
