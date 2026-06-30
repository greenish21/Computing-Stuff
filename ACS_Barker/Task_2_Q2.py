    
while True:
    factor_count = 0
    factors = []
    number = int(input("Enter a number:"))
    if number == 0:
        break
    elif number < 0:
        print("Number must be positive.")
    for i in range(1,number+1):
        if number%i==0:
            factors.append(i)
            factor_count += 1
                
    print(f"Factors for {number} are {factors}")
