from abc import ABC, abstractmethod

class Beverage(ABC):

    def __init__(self, coffe_type: str) -> None:
        self.description = f"This is a {coffe_type} coffe."

    def get_description(self) -> None:
        return self.description
    
    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError("Function not implemented")
    