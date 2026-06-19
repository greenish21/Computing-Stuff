CCA_records = {'Computer Club':40, 'Basketball':30, 
               'Cross-country':15, 'Netball':45, 
               'New Media':50, 'NCC': 100}
while True:
    CCA = input('Enter name of CCA (z to quit): ')
    if CCA == "z":
        break
    member = int(input('Enter number of members: '))
    if CCA in CCA_records:
        CCA_records[CCA] = member
    else:
        CCA_records[CCA] = member

while True:
    CCA_name = input('Enter CCA to remove:')
    if CCA_name in CCA_records:
        del CCA_records[CCA_name]
    elif CCA_name not in CCA_records:
        break
    elif CCA_records == {}:
        break