def check_case(strg):
    upper_list = []
    lower_list = []
    for letter in strg:
        if letter.isupper() == True:
            upper_list.append(letter)
        elif letter.islower() == True:
            lower_list.append(letter)
    if len(lower_list) >= 1 and len(upper_list) >= 1:
        return 'Mixed'
    else:
        return ''

def check_special(strg):
    special_list = []
    for letter in strg:
        if letter.isalnum() == False:
            special_list.append(letter)
    if len(special_list) >= 2:
        return True
    else:
        return False

def check_repeated(strg):
    repeat_list = []
    for letter in strg:
        if letter*3 in strg:
            repeat_list.append(letter)
    if len(repeat_list) >= 1:
        return True
    else:
        return False

def pw_strength(strg):
    case = check_case(strg)
    special = check_special(strg)
    repeated = check_repeated(strg)
    criteria = 0
    if case == 'Mixed':
        criteria += 1
    if special == True:
        criteria += 1
    if repeated == False:
        criteria += 1
    if criteria == 3:
        return "Unbreakable"
    elif criteria == 2:
        return "Strong"
    elif criteria == 1:
        return "Moderate"
    else:
        return "Weak"

reject = 0
while True:
    passwords = input("Enter 4 passwords in a,b,c,d format: ")
    passwords_list = passwords.split(",")
    for password in passwords_list:
        if len(password) < 8:
            reject += 1
    if reject >= 1:
        print("Every password needs to be at least 8 characters")
    else:
        break
for password in passwords_list:
    print(f"Password strength: {pw_strength(password)}")

