from src.beverages import *
from src.condiments import *

def test_espresso():
    expresso = Espresso()
    description = expresso.get_description()
    cost = expresso.cost()
    print(f"Description: {description}")
    print(f"Price: {cost}")
    assert cost == 1.99

def test_decaf():
    decaf = Decaf()
    decaf = Soy(beverage=decaf)
    decaf = Whip(beverage=decaf)
    description = decaf.get_description()
    cost = decaf.cost()
    print(f"Description: {description}")
    print(f"Price: {cost}")
    assert cost == 1.3

def test_dark_roast():
    dark_roast = DarkRoast()
    dark_roast = Mocha(beverage=dark_roast)
    dark_roast = Mocha(beverage=dark_roast)
    dark_roast = Whip(beverage=dark_roast)
    description = dark_roast.get_description()
    cost = dark_roast.cost()
    print(f"Description: {description}")
    print(f"Price: {cost}")
    assert cost == 1.49

def test_house_blend():
    house_blend = HouseBlend()
    house_blend = Milk(beverage=house_blend)
    description = house_blend.get_description()
    cost = house_blend.cost()
    print(f"Description: {description}")
    print(f"Price: {cost}")
    assert cost == .99

def main():
    test_espresso()
    test_decaf()
    test_dark_roast()
    test_house_blend()

if __name__=="__main__":
    main()
