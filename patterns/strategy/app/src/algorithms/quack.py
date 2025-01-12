from src.models.quack import QuackBehaviour


class Quack(QuackBehaviour):

    def quack():
        print("Quack!")

class Squeak(QuackBehaviour):

    def quack():
        print("Squeak!")

class MuteQuack(QuackBehaviour):

    def quack():
        print("Nothing!")
    