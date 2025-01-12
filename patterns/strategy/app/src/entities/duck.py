from src.models.fly import FlyBehaviour
from src.models.quack import QuackBehaviour

class Duck:

    def __init__(
        self, 
        species_type: str,
        fly_behaviour: FlyBehaviour = None,
        quack_behaviour: QuackBehaviour = None
    ):
        self.species_type = species_type
        self._fly_behaviour = fly_behaviour
        self._quack_behaviour = quack_behaviour
    
    @property
    def fly_behaviour(self):
        return self._fly_behaviour

    @fly_behaviour.setter
    def fly_behaviour(self, behaviour: FlyBehaviour):
        self._fly_behaviour = behaviour

    @property
    def quack_behaviour(self):
        return self._quack_behaviour

    @quack_behaviour.setter
    def quack_behaviour(self, behaviour: QuackBehaviour):
        self._quack_behaviour = behaviour
    
    def display(self):
        print(f"Looks like a {self.species_type}")
    
    def perform_quack(self):
        try:
            self._quack_behaviour.quack()
        except Exception as error:
            print(f"[perform_quack]: {error}")
    
    def perform_fly(self):
        try:
            self._fly_behaviour.fly()
        except Exception as error:
            print(f"[perform_fly]: {error}")
