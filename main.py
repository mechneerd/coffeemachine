
print('''
            / / /
        ____\_\_\____
       /    / / /    \
       \_____________/ ___
       |             |/   \
       |             |    /
       |   Coffee    |   /
       |             |  /
       |             |_/
       \_____________/
       ''')


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def paid(q, d, n, p):
    q = q * .25
    d = d * .10
    n = n * .05
    p = p * .01
    customer_paid = q + d + n + p
    return customer_paid


w = resources["water"]
m = resources["milk"]
c = resources["coffee"]


def resource(needed_ing):
    for item in needed_ing:
        if needed_ing[item] >= resource[item]:
            print(f' there is not enough {item}')

switch_on = True

cash_in_the_machine = 0
while switch_on:
    need = input("What would you like?(espresso/latte/cappuccino):")
    w = resources["water"]
    m = resources["milk"]
    c = resources["coffee"]
    i = {}
    i = MENU["espresso"]
    espresso_cost = i["cost"]

    j = {}
    j = MENU["latte"]
    latte_cost = j["cost"]

    k = {}
    k = MENU["cappuccino"]
    cappuccino_cost = k["cost"]

    if need == "espresso":
        print("Please insert coins")
        q = int(input("how many quarters?"))
        d = int(input("how many dimes?"))
        n = int(input("how many nickel?"))
        p = int(input("how many pennies?"))
        total_paid = paid(q, d, n, p)
        if total_paid >= espresso_cost:
            print(f"Enjoy the coffee")
            # TODO CASH CHANGE
            cash_in_the_machine += espresso_cost
            # TODO INGREDIENTS CHANGE
            print(resources)
            i = MENU["espresso"]
            needed_ing = i['ingredients']
            needed_water = needed_ing['water']
            needed_coffee = needed_ing['coffee']
            resources["water"] = w - needed_water
            resources["coffee"] = c - needed_coffee
            if resources["water"] <= 0 or resources["coffee"] <= 0:
                print('Not enough resource')
                cash_in_the_machine -= espresso_cost
                switch_on = False
                print(f"Take your refund ${total_paid}")
            elif total_paid > espresso_cost:
                change = total_paid - espresso_cost
                change = round(change, 2)
                print(f"Your change is ${change}")
        else:
            print("You dont have enough cash")
    elif need == "latte":
        print("Please insert coins")
        q = int(input("how many quarters?"))
        d = int(input("how many dimes?"))
        n = int(input("how many nickel?"))
        p = int(input("how many pennies?"))
        total_paid = paid(q, d, n, p)
        if total_paid >= latte_cost:
            print(f"Enjoy the coffee")
            # TODO CASH CHANGE
            cash_in_the_machine += latte_cost
            # TODO INGREDIENTS CHANGE
            print(resources)
            i = MENU["latte"]
            needed_ing = i['ingredients']
            needed_water = needed_ing['water']
            needed_coffee = needed_ing['coffee']
            needed_milk = needed_ing['milk']
            resources["water"] = w - needed_water
            resources["coffee"] = c - needed_coffee
            resources["milk"] = m - needed_milk
            if resources["water"] <= 0 or resources["coffee"] <= 0 or resources["milk"] <= 0:
                print('not enough resource')
                cash_in_the_machine -= latte_cost
                switch_on = False
                print(f"Take your refund ${total_paid}")
            elif total_paid > latte_cost:
                change = total_paid - latte_cost
                change = round(change, 2)
                print(f"Your change is ${change}")
        else:
            print("You dont have enough cash")
    elif need == "cappuccino":
        print("Please insert coins")
        q = int(input("how many quarters?"))
        d = int(input("how many dimes?"))
        n = int(input("how many nickel?"))
        p = int(input("how many pennies?"))
        total_paid = paid(q, d, n, p)
        if total_paid >= cappuccino_cost:
            print("Enjoy the coffee ")
            # TODO CASH CHANGE
            cash_in_the_machine += cappuccino_cost
            # TODO INGREDIENTS CHANGE
            print(resources)
            i = MENU["cappuccino"]
            needed_ing = i['ingredients']
            needed_water = needed_ing['water']
            needed_coffee = needed_ing['coffee']
            needed_milk = needed_ing['milk']
            resources["water"] = w - needed_water
            resources["coffee"] = c - needed_coffee
            resources["milk"] = m - needed_milk
            if resources["water"] <= 0 or resources["coffee"] <= 0 or resources["milk"] <= 0:
                print('not enough resource')
                cash_in_the_machine -= cappuccino_cost
                switch_on = False
                print(f"Take your refund ${total_paid}")
            elif total_paid > cappuccino_cost:
                change = total_paid - cappuccino_cost
                change = round(change, 2)
                print(f"Your change is ${change}")
        else:
            print("You dont have enough cash")
    print(f'Money in the machine ${cash_in_the_machine}')


