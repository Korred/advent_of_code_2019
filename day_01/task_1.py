mass_data = []

# read input data
with open('task_1_input.txt', 'r') as data:
    for line in data:
        mass_data.append(int(line))

# uses integer-division/floor divison ('//')
def required_fuel(mass):
    return (mass//3)-2

# map/calculate required fuel for each module mass and sum all fuel values
fuel_sum = sum(map(required_fuel, mass_data))

print(fuel_sum)