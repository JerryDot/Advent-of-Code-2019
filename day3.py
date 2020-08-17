def calc_path_in_wire(wire):
    current_x = current_y = step = 0
    directions = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}
    path = {}

    for section in wire:
        dx, dy = directions[section[0]]
        for r in range(int(section[1:])):
            current_x += dx
            current_y += dy
            step += 1
            if (current_x, current_y) not in path:
                path[(current_x, current_y)] = step
    return path


if __name__ == "__main__":
    with open('day3.txt', 'r') as input:
        wire1, wire2 = input.read().split()
        wire1, wire2 = wire1.split(','), wire2.split(',')    
    first_wire = calc_path_in_wire(wire1)
    second_wire = calc_path_in_wire(wire2)

    intersection_points = [point for point in first_wire if point in second_wire]
    answer_one = min(abs(x) + abs(y) for (x,y) in intersection_points)
    print("Answer for Part one: " + str(answer_one))
    answer_two = min(first_wire[point] + second_wire[point] for point in intersection_points)
    print("Answer for Part two: " + str(answer_two))

