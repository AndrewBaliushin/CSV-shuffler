from abc import ABCMeta, abstractmethod

__author__ = 'andrew'


class ShufflingStratagy():
    __metaclass__ = ABCMeta

    @abstractmethod
    def shuffle(self, input_data):
        raise NotImplementedError("There is no default implementations for this method")
