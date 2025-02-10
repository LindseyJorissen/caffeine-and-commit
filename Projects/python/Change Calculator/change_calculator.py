def calc_change_coins(change_amount):
    change_options = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    change_amount = round(change_amount * 100)

    for option in change_options:
        if change_amount == 0:
            break
        amount = change_amount // option
        if amount > 0:
            change_amount %= option
            print(f"{amount} x €{round(option / 100, 2)}")

cost = float(input("Bill price: "))
paid_amount = float(input("Enter amount paid: "))
change_amount = paid_amount - cost

print("----------------")
print(f"Bill: €{round(cost, 2)}")
print(f"Paid: €{round(paid_amount, 2)}")
print(f"Change amount: €{round(change_amount, 2)}")
calc_change_coins(change_amount)
