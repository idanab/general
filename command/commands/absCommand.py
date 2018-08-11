from abc import ABCMeta, abstractmethod


class absCommand(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def cmd_id(self):
        raise NotImplementedError

    @abstractmethod
    def command(self):
        pass