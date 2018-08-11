from observer.observables import absObserver


class CreateCsv(absObserver):

    def update(self, *args, **kwargs):
        print("createCsv observer has been called!")
        if kwargs:
            for k, v in kwargs.items():
                print(k + ": " + v)