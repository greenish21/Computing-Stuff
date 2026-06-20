serial_nos = ['523WR','924MN','1903MW','420QK','8421AB','92VC','292KS','32XC']

# Each item in the details list contains:
# [brand, model, type, width, length, height, max_speed]
details = [
    # PMDs - grouped by medium-to-large builds
    ['Telmo', 'Speed23', 'PMD', 0.7, 1.1, 1.33, 9],
    ['Lambo', 'Comfit1', 'PMD', 0.6, 1.15, 1.35, 8],
    ['Stylo', 'CoolD', 'PMD', 0.65, 1.2, 1.4, 10],
    ['Nimbus', 'SailX', 'PMD', 0.6, 0.95, 1.3, 9.5],
    ['Telmo', 'Coastie', 'PMD', 0.7, 1.1, 1.33, 10],
    ['Telmo', 'Wheeler5', 'PMD', 0.6, 1.0, 1.3, 9],
    ['Nimbus', 'SmooXth', 'Scooter', 0.3, 0.5, 1.5, 10],
    ['Lambo', 'Zipline', 'Scooter', 0.35, 0.6, 1.48, 10]
]

registered = {}
count = 0
for specification in details:
    registered[serial_nos[count]] = specification
    count += 1
del registered['1903MW']
registered['999XY'] = ['Telmo', 'Roadster', 'PMD', 0.55, 1.12, 1.45, 10]
print(registered)