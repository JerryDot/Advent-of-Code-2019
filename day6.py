with open('day6.txt', 'r') as text_input:
    orbitlist = text_input.read().split()
    orbitlist = [orbit.split(')') for orbit in orbitlist]

orbit_dict = dict()
for orbit in orbitlist:
    orbit_dict.update({orbit[1] : orbit[0]})

def count_orbits(object):
    value = 0
    if object in orbit_dict:
        value += count_orbits(orbit_dict[object])
        return value + 1
    else:
        return value

total_orbits = 0
for key in orbit_dict:
    total_orbits += count_orbits(key)

print(total_orbits)

# Answer is 151345



