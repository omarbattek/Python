from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee= CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()


is_on = True

while is_on:
    the_order = input(f"what do you want {my_menu.get_items()}")

    if the_order == "report":
        my_coffee.report()
        my_money_machine.report()
    elif the_order == "off":
        is_on = False
    else:
        find = my_menu.find_drink(the_order)
        if my_coffee.is_resource_sufficient(find) and my_money_machine.make_payment(find.cost):
            my_coffee.make_coffee(find)