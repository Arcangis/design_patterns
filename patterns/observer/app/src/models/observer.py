from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        raise NotImplementedError("Function not implemented")
