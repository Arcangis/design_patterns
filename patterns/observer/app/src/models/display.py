from abc import ABC, abstractmethod

class DisplayElement(ABC):

    @abstractmethod
    def display(self):
        raise NotImplementedError("Function not implemented")
