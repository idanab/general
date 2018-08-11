from command.commands.absCommand import absCommand


class PrintCmd(absCommand):
    cmd_id = 1

    def command(self):
        print("in PrintCmd - doing command")
