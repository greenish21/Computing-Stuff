# Task 5.1
def isvalid(timing):
    if len(timing) != 5:
        return False
    MM = timing[0:2]
    SS = timing[3:]

    if 1 <= int(MM) <= 30 and 0 <= int(SS) <= 59:
        return True
    else:
        return False
# Task 5.2
def convert(timing):
    MM = timing[0:2]
    SS = timing[3:]
    seconds = (int(MM)*60) + int(SS)
    return seconds
# Task 5.3
def average_timing(timing_list):
    len_list = len(timing_list)
    convert_list = []
    for time in timing_list:
        convert_list.append(convert(time))
    average = sum(convert_list)/len_list
    return average
# Task 5.4
def get_finalists(participant_list,timing_list):
    average = average_timing(timing_list)
    qualified_list = []
    count = 0
    for time in timing_list:
        if convert(time) < average:
            qualified_list.append(participant_list[count])
        count += 1
    return qualified_list
# Task 5.5
participant_list = []
timing_list = []
for i in range(5):
    while True:
        name = input("Input the name of the participant: ")
        time = input("Enter the timing of the participant: ")
        if isvalid(time) == True:  
            participant_list.append(name)      
            timing_list.append(time)
            break
        else:
            print("Invalid input, Try again")
finalist_list = get_finalists(participant_list,timing_list)
with open("Finalists.txt","w") as file:
    file.write("Finalists\n")
    for name in finalist_list:
        file.write(name + "\n")




