from src.objects.ducks import *
from src.algorithms.fly import *
from src.algorithms.quack import *


def main():

    mallard_duck = MallardDuck()
    mallard_duck.display()
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()

    redhead_duck = RedHeaddDuck()
    redhead_duck.display()
    redhead_duck.perform_fly()
    redhead_duck.perform_quack()

    rubber_duck = RubberDuck()
    rubber_duck.display()
    rubber_duck.perform_fly()
    rubber_duck.perform_quack()

    decoy_duck = DecoyDuck()
    decoy_duck.display()
    decoy_duck.perform_fly()
    decoy_duck.perform_quack()

    print("Someone shot the mallard duck, now it is dead!")
    mallard_duck.fly_behaviour = FlyNoWay
    mallard_duck.quack_behaviour = MuteQuack
    mallard_duck.display()
    mallard_duck.perform_fly()
    mallard_duck.perform_quack()

    print("DecoyDuck got itself installed artificial wings!")
    decoy_duck.fly_behaviour = FlyWithWings
    decoy_duck.display()
    decoy_duck.perform_fly()
    decoy_duck.perform_quack()

    print("RubberDuck turned sentient and can imitate duck language!")
    rubber_duck.quack_behaviour = Quack
    rubber_duck.display()
    rubber_duck.perform_fly()
    rubber_duck.perform_quack()

    print("RedHeadDuck is the same. Boring!")
    redhead_duck.display()
    redhead_duck.perform_fly()
    redhead_duck.perform_quack()


if __name__ == "__main__":
    main()
