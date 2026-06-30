check = [2, 7, 6, 5, 4, 3, 2]
code = ["A","B","C","D","E","F","G","H","I","Z","J"] # 1) Changed H to str
total = 0
counter = 1 # 7) Changed 0 to 1
NRIC = input("Enter the NRIC:")
while NRIC.isalnum()== False or len(NRIC)!= 9: # 9) Changed and to or
    if NRIC.isalnum()== False:
        print("Special character is not allowed!")
    else:
        print("NRIC must be 9 digits") # 2) Changed output to print
    NRIC = input("Enter the NRIC again:")
while counter<len(NRIC)-1:
    for digit in check:
        total += digit * int(NRIC[counter]) # 5) Changed str to int
        counter += 1 # 4) Changed == to +=
remainder = total%11 # 3) Changed // to %
subtract = 11 - remainder # 8) Changed order
if NRIC[-1]==code[subtract-1]: # 6) Changed 1 to -1
    print("The NRIC is valid.")
else:
    print("Invalid NRIC.")
    