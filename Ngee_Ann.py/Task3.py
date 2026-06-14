drinks = {
    'cola': {'price': 1.50, 'stock': 10, 'sold': 0},
    'soda': {'price': 1.40, 'stock': 8, 'sold': 0},
    'water': {'price': 1.00, 'stock': 15, 'sold': 0},
    'tea': {'price': 0.90, 'stock': 20, 'sold': 0}
} 

print("Drinks list:")
for drink in drinks:
    print(drink)

purchase = str(input("Enter the name of the drink you would like to purchase: ").lower())
if drinks[purchase]['stock'] > 0:
    drinks[purchase]['stock'] = drinks[purchase]['stock'] -1
    print(drinks[purchase])
    print(f"{purchase} dispensed.")
    drinks[purchase]['sold'] = drinks[purchase]['sold'] + 1
else:
    print(drinks[purchase])
    print(f"{purchase} is not available.")

total = 0
print("Summary:")
for drink in drinks:
    print(f"{drinks[drink]['sold']} {drink} sold.")
    total += drinks[drink]['sold'] * drinks[drink]['price']
print(f"Total sale is {total} for today.")

