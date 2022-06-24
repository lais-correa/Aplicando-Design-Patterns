import abc

class Veiculo(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def printVeiculo():
        pass

    def acelerar():
        pass

    def frear():
        pass