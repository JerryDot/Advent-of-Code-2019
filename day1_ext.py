fuels = [0] * 100
with open('day1.txt', 'r') as input:
    module_weights = [0] * 100
    for i in range(100):
        line = input.readline()
        module_weights[i] = int(line)

def calculate_fuel_addition(weight):
    return weight // 3 - 2

for i, f in enumerate(module_weights):
    required_fuel_addition = calculate_fuel_addition(module_weights[i])
    while required_fuel_addition > 0:
        fuels[i] += required_fuel_addition
        required_fuel_addition = calculate_fuel_addition(required_fuel_addition)

print(sum(fuels))

# answer = 4943923 