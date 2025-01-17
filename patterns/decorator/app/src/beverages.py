
from src.models.beverage import Beverage

class HouseBlend(Beverage):

    def __init__(self) -> None:
        super().__init__(HouseBlend.__name__)
    
    def cost(self) -> float:
        return .89

class DarkRoast(Beverage):

    def __init__(self) -> None:
        super().__init__(DarkRoast.__name__)
    
    def cost(self) -> float:
        return .99
    
class Espresso(Beverage):

    def __init__(self) -> None:
        super().__init__(Espresso.__name__)
    
    def cost(self) -> float:
        return 1.99
    
class Decaf(Beverage):

    def __init__(self) -> None:
        super().__init__(Decaf.__name__)
    
    def cost(self) -> float:
        return 1.05
    