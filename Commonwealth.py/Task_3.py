with open("COMPUTING_MARKS.txt", "r") as file:
    contents = file.readlines()
names = contents[0].split(",")
marks = contents[1].split(",")
names[-1] = names[-1][:-1]
for i in range(len(marks)):
    marks[i] = int(marks[i])
    

count = 0
for mark in marks:
    if mark >= 50:
        count += 1
with open("SUMMARY.txt","w") as file:
    file.write(f"Average: {sum(marks)/len(marks)}\n")
    file.write(f"Maximum: {max(marks)}\n")
    file.write(f"{names[marks.index(max(marks))]} is the top scorer\n")
    file.write(f"{count} people passed\n")
