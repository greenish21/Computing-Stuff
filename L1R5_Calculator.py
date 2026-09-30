# Task 4.1
def getgradepoint(mark):
    if mark >= 75:
        return "A1"
    elif 70 <= mark <= 74:
        return "A2"
    elif 65 <= mark <= 69:
        return "B3"
    elif 60 <= mark <= 64:
        return "B4"
    elif 55 <= mark <= 59:
        return "C5"
    elif 50 <= mark <= 54:
        return "C6"
    elif 45 <= mark <= 49:
        return "D7"
    elif 40 <= mark <= 44:
        return "E8"
    elif mark <= 39:
        return "F9"
# Task 4.2
result = {"English":0, "Higher Chinese":100, "Chemistry":0, "Geography":0, "Mathematics":0, "Physics":0,"Computing":0}
def calL1R5(result):
    english = getgradepoint(result["English"])[1]
    hcl = getgradepoint(result["Higher Chinese"])[1]
    if english < hcl:
        L1 = english
    else:
        L1 = hcl
    R5 = 0
    for i in result:
        if i != "English" and i != "Higher Chinese":
            R5 = R5 + 
    return L1
print(calL1R5(result))

