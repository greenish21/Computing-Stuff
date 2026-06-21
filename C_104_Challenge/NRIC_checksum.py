# Lookup tables for checksum
CHECKSUM_TABLE_ST = {10:"A", 9:"B", 8:"C", 7:"D", 6:"E", 5:"F", 4:"G", 3:"H", 2:"I", 1:"Z", 0:"J"}
CHECKSUM_TABLE_FG = {10:"K", 9:"L", 8:"M", 7:"N", 6:"P", 5:"Q", 4:"R", 3:"T", 2:"U", 1:"W", 0:"X"}

# Weights for each digit
WEIGHTS = [2, 7, 6, 5, 4, 3, 2]

def get_valid_nric():
    f_char = ['S','T','F','G']
    while True:
        NRIC = input("Enter a valid NRIC: ")
        if len(NRIC) == 9 and NRIC[0] in f_char and NRIC[-1].isalpha() == True and NRIC[1:-1].isdigit() == True:
            return NRIC.upper()
def calculate_weighted_sum(nric):
    middle = nric[1:-1]
    middle_list = []
    for char in middle:
        middle_list.append(int(char))
    count = 0
    sum_list = []
    for char in WEIGHTS:
        sum_list.append(char * middle_list[count])
        count += 1
    total = sum(sum_list)
    if nric[0] == 'T' or nric[0] == 'G':
        total = total + 4
    return(total)
def calculate_checksum_letter(nric, total):
    remainder = total % 11
    if nric[0] == 'S' or nric[0] == 'T':
        checksum_letter = CHECKSUM_TABLE_ST[remainder]
    elif nric[0] == 'F' or nric[0] == 'G':
        checksum_letter = CHECKSUM_TABLE_FG[remainder]
    return checksum_letter
def validate_nric(nric):
    total = calculate_weighted_sum(nric)
    checksum = calculate_checksum_letter(nric, total)
    if nric[-1] == checksum:
        return True
    else:
        return False
while True:
    nric = get_valid_nric()
    isvalid = validate_nric(nric)
    if isvalid == True:
        print(f"{nric} is valid")
    else:
        print(f"{nric} is invalid")
    proceed = str(input("Do you wish to continue? (Y/N): ")).lower()
    if proceed == 'n':
        print("Ending program")
        break
    

