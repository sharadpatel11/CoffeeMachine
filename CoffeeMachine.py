f = open("resources.txt", "r")
machine = {
    "water": int(f.readline()),
    "milk": int(f.readline()),
    "coffee": int(f.readline())
}
f.close()


def pay():
    penny = float(input("Enter the amount of pennies(1 cent): "))
    nickle = float(input("Enter the amount of nickles(5 cents): "))
    dime = float(input("Enter the amount of dimes(10 cents): "))
    quarter = float(input("Enter the amount of quarters(25 cents): "))

    return (penny * 0.01) + (nickle * 0.05) + (dime * 0.1) + (quarter * 0.25)


def make_espresso():

    resource_check = True
    if machine["water"] < 50:
        resource_check = False
        print("We're sorry! There is not enough water. Please come back later")

    if machine["milk"] < 50:
        resource_check = False
        print("We're sorry! There is not enough milk. Please come back later")

    if machine["coffee"] < 100:
        resource_check = False
        print("We're sorry! There is not enough coffee. Please come back later")

    if resource_check:
        paid = pay()
        if paid >= 2:
            if paid > 2:
                print(f"Here is your change: ${round(paid - 2, 2)}")

            machine["water"] -= 50
            machine["milk"] -= 50
            machine["coffee"] -= 100
            print("Here is your espresso ☕. Enjoy!")
        else:
            print("Insufficient fund! Please Try Again")


def make_latte():

    resource_check = True
    if machine["water"] < 50:
        resource_check = False
        print("We're sorry! There is not enough water. Please come back later")

    if machine["milk"] < 75:
        resource_check = False
        print("We're sorry! There is not enough milk. Please come back later")

    if machine["coffee"] < 125:
        resource_check = False
        print("We're sorry! There is not enough coffee. Please come back later")

    if resource_check:
        paid = pay()
        if paid >= 3.50:
            if paid > 3.50:
                print(f"Here is your change: ${round(paid - 3.50, 2)}")

            machine["water"] -= 50
            machine["milk"] -= 75
            machine["coffee"] -= 125
            print("Here is your latte ☕. Enjoy!")
        else:
            print("Insufficient fund! Please Try Again")


def make_cappuccino():

    resource_check = True
    if machine["water"] < 50:
        resource_check = False
        print("We're sorry! There is not enough water. Please come back later")

    if machine["milk"] < 100:
        resource_check = False
        print("We're sorry! There is not enough milk. Please come back later")

    if machine["coffee"] < 175:
        resource_check = False
        print("We're sorry! There is not enough coffee. Please come back later")

    if resource_check:
        paid = pay()
        if paid >= 4.25:
            if paid > 4.25:
                print(f"Here is your change: ${round(paid - 4.25, 2)}")

            machine["water"] -= 50
            machine["milk"] -= 100
            machine["coffee"] -= 175
            print("Here is your cappuccino ☕. Enjoy!")
        else:
            print("Insufficient fund! Please Try Again")


status = "on"
while status == "on":

    req = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    if req.lower() == "off":
        status = "off"
    elif req.lower() == "report":
        print(f"Water: {machine['water']}ml\nMilk: {machine['milk']}ml\nCoffee: {machine['coffee']}g")
    elif req.lower() == "add":
        machine["water"] += int(input("Add water(ml): "))
        machine["milk"] += int(input("Add milk(ml): "))
        machine["coffee"] += int(input("Add coffee(g): "))
    elif req.lower() == "espresso":
        make_espresso()
    elif req.lower() == "latte":
        make_latte()
    elif req.lower() == "cappuccino":
        make_cappuccino()
    else:
        print("Invalid order! Please try again")

f = open("resources.txt", "w")
L = [str(machine["water"]) + "\n", str(machine["milk"]) + "\n", str(machine["coffee"]) + "\n"]
f.writelines(L)
f.close()
