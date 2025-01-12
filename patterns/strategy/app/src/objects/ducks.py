from src.entities.duck import Duck
from src.algorithms.fly import *
from src.algorithms.quack import *


class MallardDuck(Duck):
    
    def __init__(self):
        super().__init__(
            species_type= "Mallard",
            fly_behaviour= FlyWithWings,
            quack_behaviour= Quack
        )

class RedHeaddDuck(Duck):
    
    def __init__(self):
        super().__init__(
            species_type= "RedHead",
            fly_behaviour= FlyWithWings,
            quack_behaviour= Quack
        )

class RubberDuck(Duck):
    
    def __init__(self):
        super().__init__(
            species_type= "RubberDuck",
            fly_behaviour= FlyNoWay,
            quack_behaviour= Squeak
        )

class DecoyDuck(Duck):
    
    def __init__(self):
        super().__init__(
            species_type= "DecoyDuck",
            fly_behaviour= FlyNoWay,
            quack_behaviour= MuteQuack
        )
    