from inspect import getmembers, isclass, isabstract

import observer.observables as observers


def update():
    for obs in observables.values():
        obs.update(name="idan", message="hello to you")


observables = {}
classes = getmembers(observers, lambda m: isclass(m) and not isabstract(m))

for name, _class in classes:
    observables[name] = _class()

update()
