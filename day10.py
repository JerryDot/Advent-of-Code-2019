from math import atan2, hypot, pi

def angle(a, b):
    return atan2(b[0] - a[0], a[1] - b[1]) % (2 * pi)

def visible(asteroids, a):
    return len(set(angle(a, b) for b in asteroids if a != b))

with open('day10.txt', 'r') as text_input:
    data = text_input.read().splitlines()

asteroids = [(x, y) for y in range(len(data))
    for x in range(len(data[0])) if data[y][x] == '#']

answer = max(visible(asteroids, a) for a in asteroids)
print(answer)

#Answer = 292


a = max(asteroids, key=lambda a: visible(asteroids, a))
asteroids.remove(a)
asteroids.sort(key=lambda b: hypot(b[0] - a[0], b[1] - a[1]))
ranks = {b : sum(angle(a, b) == angle(a, c) for c in asteroids[:i])
    for i, b in enumerate(asteroids)}
x, y = sorted(asteroids, key=lambda b: (ranks[b], angle(a, b)))[199]
print( x * 100 + y)
