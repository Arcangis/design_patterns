from abc import ABC, abstractmethod

class FlyBehaviour(ABC):

    @abstractmethod
    def fly():
        raise NotImplementedError("Function not implemented")
    