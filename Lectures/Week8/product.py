import csv

file_name = input("Enter the name of the file: ")

data = [
    ["Product ID", "Product Name", "Stock", "Price"],
    ["P001", "Laptop", 10, 1200.00],
    ["P002", "Smartphone", 15, 799.99],
    ["P003", "Headphone", 30, 149.99],
    ["P004", "Keyboard", 20, 89.99],
    ["P005", "Mouse", 25, 49.99],
    ["P006", "Monitor", 12, 299.99],
    ["P007", "External Hard Drive", 18, 109.99],
    ["P008", "USB Flash Drive", 40, 19.99],
    ["P009", "Gaming Chair", 8, 249.99],
    ["P010", "Webcam", 22, 59.99]
]

with open(file_name, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f"Data has been written to {file_name}")