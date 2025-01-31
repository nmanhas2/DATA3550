total_payroll = 0

while True:
    employee_name = input("Enter the name of an employee: (or 'done' to finish): ")
    if employee_name == 'done':
        break

    hourly_rate = float(input(f"Enter the hourly rate for {employee_name}: "))
    hours_worked = float(input(f"Enter the number of hours worked by {employee_name}: "))

    weekly_pay = hourly_rate * hours_worked
    total_payroll += weekly_pay

    print(f"Weekly pay for {employee_name}: ${weekly_pay: .2f}")

print(f"Total payroll: ${total_payroll: .2f}")