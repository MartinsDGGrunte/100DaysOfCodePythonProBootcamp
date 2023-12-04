from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()

# get the drink of choice
chosen_drink = input("What drink would you like? (espresso/latte/cappuccino)")

# print report
coffee_maker.report()

# check if sufficient resources
coffee_maker.is_resource_sufficient(chosen_drink)



