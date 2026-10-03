# Task 5.1
def calc_monthly_fee(plan_type):
    if plan_type == "basic":
        fee = 50.00
    elif plan_type == "premium":
        fee = 80.00
    elif plan_type == "vip":
        fee = 120.00
    else:
        fee = -1.0
    return fee
# Task 5.2
def calc_total_bill(plan_type, months):
    monthly_rate = calc_monthly_fee(plan_type)
    if monthly_rate == -1.0:
        return -1.0
    else:
        base_total_cost = float(monthly_rate) * months
        if months >= 12:
            return base_total_cost * 0.9
    return base_total_cost
# Task 5.3
def calc_fitness_points(total_bill):
    points = (total_bill // 5) * 2
    return int(points)
# Task 5.4
def generate_member_id(first_name, last_name):
    ID = first_name[0].upper() + last_name.upper() + "2026"
    return ID
# Task 5.5
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
while True:
    plan_type = input("Enter your plan type: ")
    months = int(input("Input your duration: "))
    if (plan_type == "basic" or plan_type == "premium" or plan_type == "vip") and months > 0:
        break
total_bill = calc_total_bill(plan_type, months)
points = calc_fitness_points(total_bill)
member_id = generate_member_id(first_name, last_name)
print(f"Your member ID is {member_id}.")
print(f"Your plan type is {plan_type} for {months} months.")
print(f"Your total bill is {total_bill}.")
print(f"You have earned {points} points.")
with open("members_log.txt","w") as file:
    file.write(f"{member_id},{plan_type},{months},{total_bill},{points}")