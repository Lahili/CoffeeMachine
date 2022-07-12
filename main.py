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

MONEY = 0


def report():
    print(f"Water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"Money: ${MONEY}")

###############  use FOR LOOP!  saves a lot of work ##############
def check_resource(selected_menu):
    for item in MENU[selected_menu]['ingredients']:
        if resources[item] < MENU[selected_menu]['ingredients'][item]:
            print(f"Sorry there is not enough {item} for {selected_menu}")
            return False
    return True
    # # print(selected_menu)
    # if resources['water'] >= MENU[selected_menu]['ingredients']['water']:
    #     # print('enough water')
    #     if resources['coffee'] >= MENU[selected_menu]['ingredients']['coffee']:
    #         # print("enough coffee")
    #         if selected_menu != 'espresso':
    #             if resources['milk'] >= MENU[selected_menu]['ingredients']['milk']:
    #                 # print('enough milk')
    #                 return True
    #             else:
    #                 print("Sorry there is not enough milk.")
    #                 return False
    #         else:  # espresso  no milk required
    #             # print('espresso no milk required')
    #             return True
    #     else:
    #         print('Sorry there is not enough coffee.')
    #         return False
    # else:
    #     print('Sorry there is not enough water.')
    #     return False


def cashier(selected_menu):
    global MONEY
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_coins = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    # print(f"total coins {total_coins}")
    price = MENU[selected_menu]['cost']
    if total_coins == 0:
        print("Sorry that's not enough money.")
    elif price > total_coins:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:  # enough money received
        change = round(total_coins - price, 2)
        print(f"Here is ${change} dollars in change.")
        MONEY += price
        return True


def barista(selected_menu):
    global resources
    for item in MENU[selected_menu]['ingredients']:
        resources[item] -= MENU[selected_menu]['ingredients'][item]
    print(f"\nHere is your {selected_menu}. Enjoy!")
    # global resources
    # resources['water'] -= MENU[selected_menu]['ingredients']['water']
    # resources['coffee'] -= MENU[selected_menu]['ingredients']['coffee']
    # if selected_menu != 'espresso':
    #     resources['milk'] -= MENU[selected_menu]['ingredients']['milk']
    # print(f"\nHere is your {selected_menu}. Enjoy!")


turnoff = False
while not turnoff:
    selected_menu = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    if selected_menu == 'report':
        report()
    elif selected_menu == 'espresso' or selected_menu == 'latte' or selected_menu == 'cappuccino':
        if check_resource(selected_menu):
            if cashier(selected_menu):
                barista(selected_menu)
    elif selected_menu == 'off':
        print("ByeBye")
        turnoff = True
    else:
        print("Please type as described in the menu")
