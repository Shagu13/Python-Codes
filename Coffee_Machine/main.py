from data import MENU, resources

profit = 0
ingredients = []


def is_resources_sufficient(order_ingredients):
    for key in order_ingredients:
        if order_ingredients[key] <= resources[key]:
            return True
        else:
            print(f"    Sorry there is not enough {key}.")
            return False


def is_money_enough(drink, quarters, dimes, nickles, pennies):
    global profit
    total_money = round((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01))
    change = total_money - drink['cost']
    if change >= 0:
        profit += drink['cost']
        print(f"Here is your ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order_ingredients):
    for key in order_ingredients:
        resources[key] -= order_ingredients[key]
    print(f"Here is your {choice} ☕. Enjoy!")


is_on = True
while is_on:
    choice = input("    What would you like (espresso/latte/cappuccino) : ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}ml.")
        print(f"Milk : {resources['milk']}ml.")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            print("Please insert the coin.")
            quarters = int(input("How many quarter? : "))
            dimes = int(input("How many dimes? : "))
            nickles = int(input("How many nickles? : "))
            pennies = int(input("How many pennies? : "))
            if is_money_enough(drink, quarters, dimes, nickles, pennies):
                make_coffee(drink['ingredients'])
