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
    hours = int(time[0:2])
    minutes = int(time[2:4])
    total_minutes = hours * 60 + minutes
    if country == "B":
        total_minutes = total_minutes + 2 * 60 + 15 + time_zone(country) * 60
    elif country == "T":
        total_minutes = total_minutes + 7 * 60 + 6 + time_zone(country) * 60
    total_minutes = total_minutes % (24 * 60)
    arrival_hours = total_minutes // 60
    arrival_minutes = total_minutes % 60
    if arrival_hours < 10:
        hours = "0" + str(arrival_hours)
    else:
        hours = str(arrival_hours)
    if arrival_minutes < 10:
        minutes = "0" + str(arrival_minutes)
    else:
        minutes = str(arrival_minutes)
    arrival_time = hours + minutes
    return arrival_time
# Main
while True:
    country = input("*** ARRIVAL TIME FOR ! ***\nB - Bangkok T - Tokyo\nEnter Option (B or T): ").upper()
    if country == "B" or country == "T":
        break
while True:
    departure_time = str(input("Enter departure time in HHMM format: "))
    if check_time(departure_time) == True:
        break
arrival_time = arrival(country,departure_time)
if arrival_time[0:2] < departure_time[0:2]:
    print(f"Arrived next day {arrival_time}")
else:
    print(f"Arrived same day {arrival_time}")

