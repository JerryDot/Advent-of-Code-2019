

def check_criteria(number):
    digits = [int(d) for d in str(number)]
    digit_no = len(digits)
    for x in range(digit_no-1):
        if digits[x] > digits[x+1]:
            return False
    double_exists = False
    for x in range(digit_no):
        if digits[(x % digit_no)] != digits[(x+1) % digit_no] == digits[(x+2) % digit_no] != digits[(x+3) % digit_no]:
            double_exists = True
    return double_exists

# Puzzle input - passwords in 108457-562041
possibilities = list()
for x in range(108457, 562041):
    if check_criteria(x):
        possibilities.append(x)

print(len(possibilities))