# Task 5.1
customer_names = ["a","b","c"]
customer_points = [15,24,12]
# Task 5.2
def display_customers(customer_names, customer_points):
    count = 0
    print("Customer List:")
    for name in customer_names:
        print(f"{name} - {customer_points[count]} points")
        count += 1
# Task 5.3
def calculate_points(amount):
    points = int(amount)//10
    return points
# Task 5.4
def update_points(customer_name, amount):
    points = calculate_points(amount)
    if customer_name in customer_names:
        i = customer_names.index(customer_name)
        customer_points[i] += points
    else:
        customer_names.append(customer_name)
        customer_points.append(points)
# Task 5.5
while True:
    display = int(input("1. View all customers\n2. Add transaction\n3. Add new customer\n4. Exit\n"))
    if display == 4:
        break
    else:
        if display == 1:
            display_customers(customer_names, customer_points)
        elif display == 2:
            name = input("Enter an existing customer name: ")
            amount = int(input("Enter the amount spent: "))
            update_points(name,amount)
        elif display == 3:
            name = input("Enter the new customer name: ")
            if name in customer_names:
                print("Customer already exists.")
            else:
                customer_names.append(name)
                customer_points.append(0)
