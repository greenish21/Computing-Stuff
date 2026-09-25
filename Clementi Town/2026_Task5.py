def load_readings():
    with open("READINGS.txt","r") as file:
        contents = file.readlines()
    strip_list = []
    for value in contents:
        strip_list.append(value.strip("\n"))
    rainfall_list = []
    for value in strip_list:
        rainfall_list.append(float(value.split(":")[1]))
    return rainfall_list
def wettest_day(readings):
    wettest = 0
    for reading in readings:
        if reading > wettest:
            wettest = reading
    count = 1
    for reading in readings:
        if wettest == reading:
            return count
        else:
            count += 1
def count_dry(readings):
    count = 0
    for reading in readings:
        if reading == 0.0:
            count += 1
    return count
def average(readings):
    total = 0
    for reading in readings:
        total = total + reading
    length = len(readings)
    average = total/length
    return round(average,2)

readings = load_readings()
print(f"There are {len(readings)} readings.")
wettest = "Day" + str(wettest_day(readings))
print(f"The wettest day is {wettest}.")
print(f"There are {count_dry(readings)} dry days.")
print(f"The average reading is {average(readings)}.")
print(readings)
while True:
    day_code = input("Enter a day code: ")
    if len(day_code) == 5:
        break
    else:
        print("Code must be 5 characters long, try again.")
day_number = int(day_code[3:5]) - 1
print(f"The rainfall recorded for {day_code} is {readings[day_number]}.")


