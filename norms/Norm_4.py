menu = {
    'osh': 25000,
    'manti': 15000,
    'lag\'mon': 15000,
    'shashlik': 15000,
}

dix = 'PROMO:uz24'
order = []
price = 0


def display_menu():
    for k, v in menu.items():
        print(f'{k} - {v}$')


def take_order():
    global order, price
    while True:
        a = input('Do u want to eat ? (y/n): ')
        if a == 'n':
            break
        elif a == 'y':
            display_menu()
            b = input('What do u want to eat ? : ').lower()
            if b in menu.keys():
                order.append(b)
                price += menu[b]
            else:
                print('Sorry try again :/ ')
        else:
            print('Sorry try again :/ \n')
    for i in order:
        print(f'{i}')
    print('it coast', price)


def apply_discount():
    global dix, price
    a = input("do u have discount ? (y/n): ")
    if a == 'y':
        pro = input('Enter a promo code : ')
        if pro == dix:
            print(price * 0.7)
    elif a == 'n':
        print(price)
    else:
        print('Sorry try again :/ \n')


def calculate_total():
    global price
    print(price)


def update_menu():
    global menu
    while True:
        a = input("Do u want to change the menu ? (y/n) : ")
        if a == 'y':
            display_menu()
            b = input('What do u want to change ? (price or name) (p/n) : ')
            if b == 'p':
                name = input("Enter the meal :").lower()
                new_p = int(input('Enter a new price : '))
                menu[name] = new_p
                display_menu()
            elif b == 'n':
                name = input("Enter the meal : ").lower()
                new_n = input('Enter a new name : ').lower()
                if name in menu.keys():
                    menu[new_n] = menu.pop(name)
                display_menu()
            else:
                print('Sorry try again :/ \n')
        elif a == 'n':
            return 0
        else:
            print('Sorry try again :/ \n')


def system():
    print('1. MENU', '2. TAKE ORDER', '3. DISCOUNT', '4. TOTAL', '5. CHANGE THE MENU', sep='\n')
    a = int(input('What so u want ? enter a num : '))
    if a == 1:
        display_menu()
    elif a == 2:
        take_order()
    elif a == 3:
        apply_discount()
    elif a == 4:
        calculate_total()
    elif a == 5:
        update_menu()


system()
