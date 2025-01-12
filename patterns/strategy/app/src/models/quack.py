from abc import ABC, abstractmethod

class QuackBehaviour(ABC):

    @abstractmethod
    def quack():
        raise NotImplementedError("Function not implemented")
    