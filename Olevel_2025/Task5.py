# Task 5.4
def total_cost(cost):
    return round(cost*(109/100),2) # Returns the rounded value of cost + 9% tax

def discount(cost):
    total = total_cost(cost)
    if total >= 50 and total < 100: # Evaluates range of values from 50 inclusive to 100 exclusive
        deduction = total * 0.95
    elif total >= 100: # Evaluates range of values greater or equal to 100
        deduction = total * 0.9
    else:
        deduction = total 
    return round(deduction,2)

def reward_points(total_cost):
    reward_points = int(total_cost) * 3 # Floors the total cost to the lowest whole number, and finds the reward points
    return reward_points

def voucher(total_cost, first_name):
    if total_cost > 25 and total_cost <= 50:
        voucher_code = first_name[0:3] + "05PERCENT" # Adds first 3 characters of name to string
    elif total_cost > 50:
        voucher_code = first_name[0:3] + "10PERCENT" # Adds first 3 characters of name to string
    else:
        voucher_code = None # Voucher code is none if no conditions are met
    return voucher_code

first_name = str(input("Input your first name: ")) # Input for first name
sale_cost = float(input("Enter the cost of your sale: ")) # Input for the initial cost
print("Receipt")
print(f"The total cost of the sale is ${total_cost(sale_cost)}") # Outputs initial cost with tax
print(f"The discounted cost of the sale is ${discount(sale_cost)}") # Outputs discount based on amount in initial cost with tax
discounted = discount(sale_cost)
print(f"You get {reward_points(discounted)} reward points") # Finds the amount of reward points
final_voucher = voucher(discounted, first_name)
if final_voucher == None: # Finds if the user is eligible for a voucher code
    print("You need to spend over $25 for a voucher code.")
else:
    with open("vouchercode.txt","w") as file: 
        file.write(final_voucher) # Writes voucher code to text file