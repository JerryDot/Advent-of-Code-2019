with open('day1.txt', 'r') as input:
    line = input.readline()
    fuel_sum = 0
    while line:
        fuel_addition = int(line) // 3 - 2
        fuel_sum = fuel_sum + fuel_addition
        line = input.readline()
    print(fuel_sum)
