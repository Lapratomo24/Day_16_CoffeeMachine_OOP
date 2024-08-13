from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Using OOP to create the same output as Day 15

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
turn_off = False

# coffee machine is on
while not turn_off:
    options = menu.get_items()
    selection = input("What would you like? Type 'cappuccino', 'latte', or 'espresso': ")
    if selection == "off":
        turn_off = True
        print("Machine turned off.")
    elif selection == "report":
        # create a report of ingredients and profit
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(selection)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
