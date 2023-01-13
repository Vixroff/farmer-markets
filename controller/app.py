from controller.handlers.handler import handler


GREETINGS = """

                ***Welcome to the FarmMarkets application!***
        Here you can find all informations about farmers markets you interested
        -----------------------------------------------------------------------

        Enter [guide] command to get instruction
        """


def start():
    print(GREETINGS)
    while True:
        cmd = input('==> Enter a command: ')
        handler(cmd)


if __name__ == "__main__":
    start()
