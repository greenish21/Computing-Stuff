names = ['Ann','Ben','Cal','Dan','Eve']
marks = [80,65,54,38,72]

print("Calculating grades and statistics…")
# Task 5.1
def calculate_grades(marks):
    grades = []
    for mark in marks:
        if 70<=mark<=100:
            grades.append("A1")
        elif 60<=mark<=69:
            grades.append("B2")
        elif 50<=mark<=59:
            grades.append("C3")
        elif 0<=mark<=49:
            grades.append("F4")
    return grades
# Task 5.2
def top_student(names,marks):
    top_score = 0
    for mark in marks:
        if mark > top_score:
            top_score = mark
    i = marks.index(top_score)
    return names[i]
# Task 5.3
def statistics(names,marks,grades):
    resultlist = []
    passed_count = 0
    for mark in marks:
        if mark >= 50:
            passed_count += 1
    resultlist.append((passed_count/len(marks))*100)
    MSG_sum = 0
    MSG_len = len(grades)
    for grade in grades:
        MSG_sum += int(grade[1])
    MSG = MSG_sum/MSG_len
    resultlist.append(MSG)
    resultlist.append(top_student(names,marks))
    return resultlist
# Task 5.4
def display_result(names,marks,grades,resultlist):
    print("Student Results")
    count = 0
    for name in names:
        print(f"{name}: {marks[count]}  (Grade: {grades[count]})")
        count += 1
    print(f'\nPercentage passes = {resultlist[0]}')
    print(f"MSG = {resultlist[1]}")
    print(f"Top student = {resultlist[2]}")
# Task 5.5
def write_file(names,marks,grades,resultlist):
    with open("OUTPUTFILE.TXT","w") as file:
        file.write("Student Results\n")
        count = 0
        for name in names:
            file.write(f"{name}: {marks[count]}  (Grade: {grades[count]})\n")
            count += 1
        file.write(f'\nPercentage passes = {resultlist[0]}\n')
        file.write(f"MSG = {resultlist[1]}\n")
        file.write(f"Top student = {resultlist[2]}\n")
# Task 5.6
grades = calculate_grades(marks)
resultlist = statistics(names,marks,grades)
options = input("Option 1: Display result on screen\nOption 2: Write results to file OUTPUT.TXT\n")
if options == "1":
    display_result(names,marks,grades,resultlist)
elif options == "2":
    write_file(names,marks,grades,resultlist)




    