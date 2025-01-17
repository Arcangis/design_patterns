from abc import ABC

from src.models.beverage import Beverage

class CondimentDecorator(Beverage, ABC):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage
