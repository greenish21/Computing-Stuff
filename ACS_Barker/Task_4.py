num_student = 7
valid_list = []
for i in range(num_student):   
    while True:    
        data = input(f"Enter the attendance for student {i+1}: ")
        if len(data) == 9:
            data_list = data.split(" ")
            if len(data_list) == 5:
                valid = True
                for num in data_list:
                    if num != "0" and num != "1":
                        print("Invalid input")
                        valid = False
                if valid == True:
                    valid_list.append(data_list)
                    break
            else:
                print("Invalid input")
        else:
            print("Invalid input")
total_attendance = 0
count = 1
for student in valid_list:
    day_count = 0
    for attendance in student:
        if attendance == "1":
            total_attendance += 1
            day_count += 1
    print(f"Student {count}         {day_count} day(s)")
    count += 1

total_possible_attendance = num_student * 5
present_rate = (int(total_attendance)/int(total_possible_attendance) * 100)
print(f"Present rate = {present_rate:.1f}%")

count = 1
for student in valid_list:
    day_count = 0
    for attendance in student:
        if attendance == "1":
            day_count += 1
    if day_count == 5:
        print(f"Student {count} has perfect attendance")
    count += 1



               
               

        



