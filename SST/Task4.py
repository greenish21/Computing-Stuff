def validate_SString(s_string):
    valid = True
    for letter in s_string:
        if letter == "A" or letter == "C" or letter == "G" or letter == "U":
            pass
        else:
            valid = False
    return valid

def validate_PString(p_string,s_string_length):
    valid = True
    count_left_p = 0
    count_right_p = 0
    if len(p_string) != s_string_length:
        valid = False
    for character in p_string:
        if character != "*" and character != "(" and character != ")":
            valid = False
        elif character == "(":
            count_left_p += 1
        elif character == ")":
            count_right_p += 1
    if count_left_p != count_right_p:
        valid = False
    return valid

while True:
    choice = input("Proceed with analysis? (y to proceed, q to exit) ")
    if choice == "y":
        while True:
            S_input = input("Enter S: ").upper()
            if validate_SString(S_input) == True:
                break
            else:
                print("Invalid S, Try again.")
        while True:
            P_input = input("Enter P: ")
            if validate_PString(P_input,len(S_input)) == True:
                break
            else:
                print("Invalid P, Try again.")
        countA = 0
        countC = 0
        countG = 0
        countU = 0
        for char in S_input:
            if char == "A":
                countA += 1
            if char == "C":
                countC += 1
            if char == "G":
                countG += 1
            if char == "U":
                countU += 1
        display_list = [["A", countA], ["C", countC], ["G", countG], ["U", countU]]
        new_list = []
        while len(display_list) > 0:
            biggest = display_list[0]
            for item in display_list:
                if item[1] > biggest[1]:
                    biggest = item
            new_list.append(biggest)
            display_list.remove(biggest)
        count = 0
        for i in new_list:
            print(new_list[count])
            count += 1
        S_list = list(S_input)
        P_list = list(P_input)
        base_list = []
        base_count = 0
        for base in S_list:
            if P_list[base_count] == "*":
                base_list.append(base)
            base_count += 1

        max_letter = base_list[0]
        max_count = 0
        for letter in base_list:
            count = 0
            for x in base_list:
                if letter == x:
                    count += 1
            if count > max_count:
                max_count = count
                max_letter = letter
        print(f"The base with the highest count of * is {max_letter} at {max_count}")
    elif choice == "q":
        break
        
