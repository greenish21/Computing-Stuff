def time_zone(country):
    if country == "B":
        return -1
    else:
        return 1
def check_time(time):
    if time.isdigit() and len(time) == 4:
        if int(str(time)[0:2]) >= 0 and int(str(time)[0:2]) <= 23:
            if int(str(time)[2:4]) >= 0 and int(str(time)[2:4]) <= 59:
                return True
    return False
def arrival(country,time):
    hours = time[0:2]
    minutes = time[2:4]
    arrival_adjust = time_zone(country)
    if country == "B":
        arrival_time = str(int(hours)+2+arrival_adjust) + str(int(minutes)+15)
    elif country == "T":
        arrival_time = str(int(hours)+7+arrival_adjust) + str(int(minutes)+6)


    
    print(arrival_time)
arrival("T","1200")