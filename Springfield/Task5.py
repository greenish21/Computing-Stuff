# Task 5.1
current_masked_card = None
def validate_card_manual():
    while True:
        raw_string = input("Enter your raw credit card string: ")
        if len(raw_string) == 19:
            if raw_string[4] == "-" and raw_string[9] == "-" and raw_string[14] == "-":
                if raw_string[0:4].isdigit() and raw_string[5:9].isdigit() and raw_string[10:14].isdigit() and raw_string[15:19].isdigit():
                    break
        print("Invalid input, try again.")
    return raw_string
# Task 5.2
def mask_card_logic(card_number):
    masked_num = ""
    last_four = card_number[-4:]
    hidden_num = len(card_number) - 4
    masked_num = masked_num + (hidden_num * "*") + last_four
    return masked_num
# Task 5.3
def run_masker():
    global current_masked_card
    card_number = validate_card_manual()
    clean_card_data = card_number
    current_masked_card = mask_card_logic(card_number)
    print(current_masked_card)
    if current_masked_card[-4:] == clean_card_data[-4:] and current_masked_card[:-4].count('*') == 15:
        print("Verification Check: SUCCESS")
    else:
        print("Verification Check: FAILED")
# Task 5.4
while True:
    options = int(input("Choose an option:\n1. Enter credit card number and mask the credit card\n2. Write the masked credit card to a file\n3. Exit the program\n"))
    if options == 1:
        run_masker()
    elif options == 2:
        if current_masked_card != None:
            with open("masked_credit_card.txt","w") as file:
                file.write(current_masked_card)
        else:
            print("There is no masked credit card number avaliable.")
    elif options == 3:
        break




