total_bill = 0
item_name = ""
item_price = 0
quantity = 0

while True:
    item_name= input("Enter the name of an item (or 'done' to stop): ")
    if item_name == 'done':
        break
    item_price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity: "))
    total_bill += item_price * quantity
    print(f"Cost for {item_name}(s) : ${item_price}")

print(f"Final Bill Summary: ${total_bill: .2f}")