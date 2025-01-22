date = input("What is the date in the format mm/dd: ")
price = float(input("Enter the price: "))

if date == "09/24":
    if price < 128:
        discount = price * 0.08
    else:
        discount = price * 0.16
else:
    discount = 0

actual_price = price - discount

print(f"Actual price ${actual_price:.2f}")