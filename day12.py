#Input:
#<x=1, y=3, z=-11>
#<x=17, y=-10, z=-8>
#<x=-1, y=-15, z=2>
#<x=12, y=-4, z=-4>
import numpy as np
from operator import add

class Moon:
    def __init__(self, initial_position):
        self.initial_position = initial_position
        self.position = initial_position
        self.velocity = [0,0,0]
    
    def get_initial_position(self, dimension=4):
        if dimension == 4:
            return self.initial_position
        #else:
        #    return self.initial_position[dimension]
    
    def get_position(self, dimension=4):
        if dimension == 4:
            return self.position
        #else:
        #    return self.position[dimension]

    def increment_position(self):
        self.position = list(map(add, self.position, self.velocity))
    
    def get_velocity(self, dimension=4):
        if dimension == 4:
            return self.velocity
        #else:
        #    return self.velocity[dimension]

    def increment_velocity(self, component, direction):
        self.velocity[component] += direction

moon1 = Moon([1,3,-11])
moon2 = Moon([17,-10,-8])
moon3 = Moon([-1,-15,2])
moon4 = Moon([12,-4,-4])
moons = [moon1, moon2, moon3, moon4]


def calculate_energy(moon):
    positional_energy = abs(moon.get_position()[0]) + abs(moon.get_position()[1]) + abs(moon.get_position()[2])
    kinetic_energy = abs(moon.get_velocity()[0]) + abs(moon.get_velocity()[1]) + abs(moon.get_velocity()[2])
    return positional_energy * kinetic_energy

def check_for_initial_state(moon, dimension):
    if moon.get_position(dimension) == moon.get_initial_position(dimension):
        if moon.get_velocity(dimension) == 0:
            return True 

if __name__ == "__main__":
    print('hi')
    for t in range(1000):
        for moon in moons:
            for moony in moons:
                for i in range(3):
                    if moon.get_position()[i] > moony.get_position()[i]:
                        moon.increment_velocity(i, -1)
                    elif moon.get_position()[i] < moony.get_position()[i]:
                        moon.increment_velocity(i, 1)
        
        for moon in moons:
            moon.increment_position()
        #position = moon1.get_position()

        #if check_for_initial_state(moon1, 0) and check_for_initial_state(moon2, 0) and check_for_initial_state(moon3, 0) and check_for_initial_state(moon4 , 0):
        #   print("x  " + str(t))
        #if check_for_initial_state(moon1, 1) and check_for_initial_state(moon2, 1) and check_for_initial_state(moon3, 1) and check_for_initial_state(moon4 , 1):
        #    print("y  " + str(t))
        #if check_for_initial_state(moon1, 2) and check_for_initial_state(moon2, 2) and check_for_initial_state(moon3, 2) and check_for_initial_state(moon4 , 2):
            print("z  " + str(t))

    print( calculate_energy(moon1) + calculate_energy(moon2) + calculate_energy(moon3) + calculate_energy(moon4))

# Part 2 incomplete
    

