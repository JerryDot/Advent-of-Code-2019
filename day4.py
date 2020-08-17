possibilities = set()

def check_criteria(number):
    digits = [int(d) for d in str(number)]
    for x in range(len(digits)-1):
        if digits[x] > digits[x+1]:
            return False
    if len(digits) == len(set(digits)):
        return False
    return True

# Puzzle input - passwords in 108457-562041
for x in range(108457, 562041):
    if check_criteria(x):
        possibilities.add(x)

print(possibilities)
print(len(possibilities))
