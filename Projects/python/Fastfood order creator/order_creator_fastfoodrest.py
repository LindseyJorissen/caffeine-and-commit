menu = [{"item" : "Chicken Strips", "price" : "$3.50"},
        {"item" : "French Fries", "price" : "$2.50"},
        {"item" : "Salad", "price" : "$3.75"},
        {"item" : "Hamburger", "price" : "$4.00"},
        {"item" : "Hotdog", "price" : "$3.50"},
        {"item" : "Small Drink", "price" : "$1.25"},
        {"item" : "Medium Drink", "price" : "$1.50"},
        {"item" : "Large Drink", "price" : "$1.75"},
        {"item" : "Milk Shake", "price" : "$2.25"}]

def print_menu(menu):
    for index, item in enumerate(menu, start=1):
        print(f"{index}: {item['item']} - {item['price']}")

print_menu(menu)
print("Type the entire order in one line. For example: Hamburger with french fries = 32 ")
order = input("Enter an order:\n -> ")

