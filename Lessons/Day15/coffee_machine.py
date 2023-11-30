import menu


def start():
    machine_on = True
    while machine_on:
        user_choice = input("What would you like? (espresso/latte/capuccino): ")
        if user_choice == "espresso" or user_choice == "latte" or user_choice == "capuccino":
            if check_if_resources_are_sufficient(user_choice):
                money_inserted = process_coins()
                cost_of_drink = menu.MENU[user_choice]["cost"]
                if money_inserted >= cost_of_drink:
                    process_payment(money_inserted, cost_of_drink)
                    update_ingredients(user_choice)
                    print(f'Here is your {user_choice}. Enjoy!')
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                print("Can't make drink insufficient ingredients.")
        elif user_choice == "off":
            machine_on = False
        elif user_choice == "report":
            print(f'Water: {menu.resources["water"]}ml')
            print(f'Milk: {menu.resources["milk"]}ml')
            print(f'Coffee: {menu.resources["coffee"]}g')
            print(f'Money: {menu.resources["money"]}$')
        else:
            print("Unsupported option! Please try again!")


def check_if_resources_are_sufficient(drink):
    enough_water = False
    if drink == "espresso":
        enough_milk = True
    else:
        enough_milk = False
    enough_coffee = False

    remaining_water = menu.resources["water"]
    remaining_milk = menu.resources["milk"]
    remaining_coffee = menu.resources["coffee"]

    if drink == "espresso":
        required_water = menu.MENU[drink]["ingredients"]["water"]
        required_coffee = menu.MENU[drink]["ingredients"]["coffee"]
    else:
        required_water = menu.MENU[drink]["ingredients"]["water"]
        required_coffee = menu.MENU[drink]["ingredients"]["coffee"]
        required_milk = menu.MENU[drink]["ingredients"]["milk"]

    if remaining_water >= required_water:
        enough_water = True
    else:
        print("Sorry there is not enough water.")

    if drink != "espresso":
        if remaining_milk >= required_milk:
            enough_milk = True
        else:
            print("Sorry there is not enough milk.")

    if remaining_coffee >= required_coffee:
        enough_coffee = True
    else:
        print("Sorry there is not enough coffee.")

    if enough_water and enough_milk and enough_coffee:
        return True
    else:
        return False


def process_coins():

    quarter_value = 0.25
    dimes_value = 0.10
    nickles_value = 0.05
    pennies_value = 0.01

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    value_of_coins_inserted = (quarter_value * quarters + dimes_value * dimes + nickles_value * nickles
                               + pennies_value * pennies)
    print(round(value_of_coins_inserted, 2))

    return round(value_of_coins_inserted, 2)


def process_payment(money_inserted, cost_of_drink):

    menu.resources["money"] += money_inserted

    if money_inserted > cost_of_drink:
        change = money_inserted - cost_of_drink
        menu.resources["money"] -= change
        print(f'Here is ${round(change, 2)} in change.')


def update_ingredients(drink):

    menu.resources["water"] -= menu.MENU[drink]["ingredients"]["water"]
    menu.resources["coffee"] -= menu.MENU[drink]["ingredients"]["coffee"]

    if drink != "espresso":
        menu.resources["milk"] -= menu.MENU[drink]["ingredients"]["milk"]


start()
