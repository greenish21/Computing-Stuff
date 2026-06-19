import random

numbers = []
for i in range(2):
    num = random.randint(65, 90)
    while num in numbers: # 1) Changed '==' to 'in'
        num = random.randint(65, 90)
    numbers.append(num) # 2) Changed '-' to append 

numbers[0] = numbers[0] + 2
if numbers[0] > 90:
    numbers[0] = numbers[0] # 4) Changed number to numbers

secret_string = chr(numbers[0]) + chr(numbers[1])
for chance in range(5):
    positions = [] # 9) Moved positions into for loop
    guess = input(f'Chance {chance + 1}: ').upper()   
    for i in range(len(secret_string)): # 5) Changed to secret string
        if secret_string[i] in guess:
            positions = positions.append(i) # 7) Changedd to append
    if positions != []: # 8) Changed == to !=
        print('Found at positions:',positions)
    else:
        print('Not found')
    to_guess = input('Do you want to guess?') # 3) Removed excess indentation
    if to_guess in ['Y','y']: # 6) Changed to list
        continue

final_guess = input('Guess the 2-letter string: ').upper()
if final_guess == secret_string:
    print('Correct!')
else:
    print('Wrong')