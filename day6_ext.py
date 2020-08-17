with open('day6.txt', 'r') as text_input:
    orbitlist = text_input.read().split()
    orbitlist = [orbit.split(')') for orbit in orbitlist]

orbit_dict = dict()
for orbit in orbitlist:
    orbit_dict.update({orbit[1] : orbit[0]})

def orbital_transfer_down(object):
    new_orbit = orbit_dict[orbit_dict[object]]
    orbit_dict.update({object : new_orbit})

santa = 'SAN'
you = 'YOU'
com = 'COM'

def create_orbit_chain(object):
    orbit_chain = list()
    orbit_chain.append(orbit_dict[object])
    while orbit_dict[object] != com:
        orbital_transfer_down(object)
        orbit_chain.append(orbit_dict[object])
    return orbit_chain

santa_list = create_orbit_chain(santa)
you_list = create_orbit_chain(you)

distances = list()
for i, x in enumerate(santa_list):
    for j, y in enumerate(you_list):
        if x == y:
            distances.append(i+j)

print(min(distances))
# Answer is 391


