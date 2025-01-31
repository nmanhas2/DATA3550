total_revenue = 0
total_count = 0

for customer in range(6):
    print(f"Processing customer {customer + 1}: ")
    
    while True:
        ticket_price = float(input("Enter the ticket price (or -1 to finish: ): "))
        if ticket_price == -1:
            break
        total_revenue += ticket_price
        total_count += 1

print(f"{total_count} tickets sold for {total_revenue}")
