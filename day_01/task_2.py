mass_data = []

# read input data
with open('task_1_input.txt', 'r') as data:
    for line in data:
        mass_data.append(int(line))

# additionaly calculates additional fuel needed for the initially added fuel
def required_fuel(mass):
    fuel_values = [(mass//3)-2]
    while True:
        fuel_to_add = (fuel_values[-1]//3)-2
        if (fuel_to_add > 0):
            fuel_values.append(fuel_to_add)
        else:
            break

    return sum(fuel_values)

fuel_sum = sum(map(required_fuel, mass_data))

print(fuel_sum)