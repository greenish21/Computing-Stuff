#Task 4#
def odd_parity(bits):
    if bits % 2 == 1:
        return True
    else:
        return False
def even_parity(bits):
    if bits % 2 == 0:
        return True
    else:
        return False
def clean_data(raw_data):
    clean_str = ""
    for char in raw_data:
        if char.isalnum() == True:
            clean_str = clean_str + char
    return clean_str
def validate_data(raw_data):
    digit_list = []
    for char in raw_data:
        if char.isdigit() == True:
            digit_list.append(char)
    for num in digit_list:
        if num != "0" and num != "1":
            return "Invalid"
    return "Valid"

while True:
    parity_choice = input("*** PARITY CHECK SYSTEM! ***\nE - Even Parity\nO - Odd Parity\nEnter Choice (E or O): ").upper()
    if parity_choice == "E" or parity_choice == "O":
        break
    else:
        print("Invalid Input, Try Again.")
data = input("Enter your data: ")
if validate_data(data) == "Invalid":
    print("Invalid Input")
else:
    cleaned_data = clean_data(data)
    count = 0
    for char in cleaned_data:
        if char == 1:
            count += 1
    if parity_choice == "E":
        if even_parity(count) == True:
            print("No error detected")
        else:
            print("Error detected")
    elif parity_choice == "O":
        if odd_parity(count) == True:
            print("No error detected")
        else:
            print("Error detected")
