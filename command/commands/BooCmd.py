from command.commands.absCommand import absCommand


class BooCmd(absCommand):
    cmd_id = 2

    def command(self):
        print("in BooCmd - Boo!!!!!")
