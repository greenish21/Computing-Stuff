
# Question 1 — Predicting Weather Type
day_ids = [
    'D001', 'D002', 'D003', 'D004', 'D005',
    'D006', 'D007', 'D008', 'D009', 'D010',
    'D011', 'D012', 'D013', 'D014', 'D015'
]

# Each item contains:
# [temperature, humidity, wind_speed, weather_type]
weather_data = [
    [32.1, 68, 10, 'Sunny'],
    [31.5, 72, 12, 'Sunny'],
    [33.0, 65, 8, 'Sunny'],
    [30.8, 74, 11, 'Sunny'],

    [25.2, 92, 21, 'Rainy'],
    [24.8, 95, 18, 'Rainy'],
    [26.0, 90, 20, 'Rainy'],
    [25.5, 88, 23, 'Rainy'],

    [28.2, 83, 22, 'Cloudy'],
    [27.8, 85, 24, 'Cloudy'],
    [29.0, 80, 19, 'Cloudy'],
    [28.5, 82, 21, 'Cloudy'],

    [30.0, 89, 28, 'Stormy'],
    [29.2, 91, 30, 'Stormy'],
    [30.5, 87, 27, 'Stormy']
]
count = 0
weather_records = {}
for i in weather_data:
    weather_records[day_ids[count]] = i
    count += 1
del weather_records['D003']
weather_records['D016'] = [31.8, 70, 9, 'Sunny']


temperature = float(input("Enter the temperature now: "))
humidity = float(input("Enter the humidity now: "))
wind_speed = float(input("Enter the wind speed now: "))

shortest_distance = 99999
prediction = ""

for i in weather_records:
    data = weather_records[i]
    existing_temp = data[0]
    existing_humidity = data[1]
    existing_wind = data[2]
    distance = ((temperature-existing_temp)**2+(humidity-existing_humidity)**2+(wind_speed-existing_wind)**2)**0.5
    if distance < shortest_distance:
        shortest_distance = distance
        prediction = data[3]
        day_id = i
print(f"The nearest day ID is {day_id}")
print(f"Predicted weather is {prediction}")

