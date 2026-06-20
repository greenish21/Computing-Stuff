conversion_factors = {
      "B": 1,
      "kB": 1000,
      "MB": 1000**2,
      "KiB": 1024,
      "MiB": 1024**2
  }
conversion_factors['GB'] = 1000**3
conversion_factors['TB'] = 1000**4
conversion_factors['PB'] = 1000**5

conversion_factors['GiB'] = 1024**3
conversion_factors['TiB'] = 1024**4
conversion_factors['PiB'] = 1024**5


def list_units():
    count = 1
    print("Available Units: ")
    for key in conversion_factors:
        print(f"{count}: {key}")
        count += 1
def is_valid_unit(unit):
    if unit in conversion_factors:
        return True
    else:
        return False
def convert_storage(value, from_unit, to_unit):
    value = int(value)
    from_factor = conversion_factors[from_unit]
    to_factor = conversion_factors[to_unit]
    
    value = value * from_factor
    value = value / to_factor
    return value

while True:
    list_units()
    while True:
        number = input("Enter a number to convert: ")
        if not number.isdigit:
            print("You must enter a valid number")
        elif int(number) < 1:
            print("You must enter a positive number")
        else:
            break
    while True:
        from_unit = input("Enter the from unit to convert from: ")
        if is_valid_unit(from_unit):
            break
        else:
            print(f"{from_unit} is not a valid unit. ")
    while True:
        to_unit = input("Enter the to unit to convert to: ")
        if is_valid_unit(to_unit):
            break
        else:
            print(f"{to_unit} is not a valid unit. ")
    converted = convert_storage(number, from_unit, to_unit)
    print(f"{number} {from_unit} is {round(converted,4)} {to_unit}")
    proceed = input("Do you want to continue? Type 'no' to end the program or any key to continue: ").lower()
    if proceed == "no":
        print("Exiting program... Bye.")
        break
