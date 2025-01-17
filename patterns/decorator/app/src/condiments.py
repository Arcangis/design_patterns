from src.models.beverage import Beverage
from src.decorators.condiment import CondimentDecorator

class Milk(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        super().__init__(beverage)

    def get_description(self):
        return self.beverage.get_description() + " With milk."
    
    def cost(self):
        return self.beverage.cost() + .1

class Mocha(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        super().__init__(beverage)

    def get_description(self):
        return self.beverage.get_description() + " With mocha."
    
    def cost(self):
        return self.beverage.cost() + .2

class Soy(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        super().__init__(beverage)

    def get_description(self):
        return self.beverage.get_description() + " With soy."
    
    def cost(self):
        return self.beverage.cost() + .15
    
class Whip(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        super().__init__(beverage)

    def get_description(self):
        return self.beverage.get_description() + " With whip."
    
    def cost(self):
        return self.beverage.cost() + .1
    