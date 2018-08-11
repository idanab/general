from inspect import getmembers, isclass, isabstract

import command.commands as commands

classes = getmembers(commands, lambda m: isclass(m) and not isabstract(m))

for name, _class in classes:
    inst = _class()
    inst.command()
