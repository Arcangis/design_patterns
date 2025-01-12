from src.models.fly import FlyBehaviour


class FlyWithWings(FlyBehaviour):

    def fly():
        print("I'm flying!")

class FlyNoWay(FlyBehaviour):

    def fly():
        print("Nothing!")
    