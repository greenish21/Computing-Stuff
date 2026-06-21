
name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0 # 4) Changed count to 0

flag = True
while flag == True: # 3) Changed False to True
    name = input('Enter student\'s name: ') # 1) Added \'
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100: # 7) Changed or to and
            break
        else:
            print('Invalid mark!')
    mark_list += [mark] # 8) Removed indentation
    count += 1
    if mark >= 75: # 10) Changed > to >=
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name] # 6) Changed () to []
    more = str(input('Would you like to enter another score, Y or N?: ')) # 5) Changed int to str
    if more == 'N':
        flag = False
average = round(sum(mark_list)/len(mark_list), 2) # 2) Changed max to sum
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.") # 9) convereted count to string
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))