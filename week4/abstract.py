from abc import ABCMeta, abstractmethod

class Sender(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        pass

class Child(Sender): 
    def send(self):
        pass

Child()
