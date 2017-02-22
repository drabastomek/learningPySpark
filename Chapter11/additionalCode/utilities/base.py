from abc import ABCMeta, abstractmethod

class BaseConverter(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def convert(f, t):
        raise NotImplementedError

if __name__ == '__main__':
    i = BaseConverter()