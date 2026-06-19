
print("Choose (1,2,3)")
print("1. 2.4 km Run")
print("2. Standing Broad Jump")
print("3. Exit program")
while True:    
    selection = input("Please select 1 / 2 / 3: ")
    if selection == "1":
        timing = round(float(input("Enter timing: ")), 1)
        if timing < 10.4:
            grade = "A"
        elif timing <= 11.4 and timing >= 10.4:
            grade = "B"
        elif timing <= 12.4 and timing >= 11.41:
            grade = "C"
        else:
            grade = "F"
        print(f"2.4 KM run timing {timing} Grade {grade}")
    elif selection == "2":
        distance = round(float(input("Enter distance: ")))
        if distance > 237:
            grade = "A"
        elif distance <= 237 and distance >= 228:
            grade = "B"
        elif distance <= 227 and distance >= 218:
            grade = "C"
        else:
            grade = "F"
        print(f"Standing Broad Jump distance {distance} grade {grade}")
    elif selection == "3":
        print("Program ends.")
        break