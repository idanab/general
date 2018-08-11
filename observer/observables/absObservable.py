from abc import ABCMeta, abstractmethod


class absObserver(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        """update observer of some event"""
        pass