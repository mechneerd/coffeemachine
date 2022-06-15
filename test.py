if need == "espresso":
    print("Please insert coins")
    q = int(input("how many quarters?"))
    d = int(input("how many dimes?"))
    n = int(input("how many nickel?"))
    p = int(input("how many pennies?"))
    total_paid = paid(q, d, n, p)
    if total_paid >= espresso_cost:
        print("Enjoy the coffee")
        # TODO CASH CHANGE
        cash_in_the_machine += espresso_cost
        # TODO INGREDIENTS CHANGE
        i = MENU["espresso"]
        needed_ing = i['ingredients']
        needed_water = needed_ing['water']
        needed_coffee = needed_ing['coffee']
        resources["water"] = w - needed_water
        resources["coffee"] = c - needed_coffee
        print(resources)
        if total_paid > espresso_cost:
            change = total_paid - espresso_cost
            change = round(change, 2)
            print(f"Your change is {change}")
    else:
        print("You dont have enough cash")