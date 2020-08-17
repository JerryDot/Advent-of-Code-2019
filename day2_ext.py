with open('day2.txt', 'r') as codestring:
    codelist = codestring.read().split(',')
    codelist = list(map(int, codelist))

def run_computer(noun, verb):
    test_codelist = codelist.copy()
    test_codelist[1] = noun
    test_codelist[2] = verb
    head = 0
    while test_codelist[head] != 99:
        if test_codelist[head] == 1:
            test_codelist[test_codelist[head+3]] = test_codelist[test_codelist[head+1]] + test_codelist[test_codelist[head+2]]
        if test_codelist[head] == 2:
            test_codelist[test_codelist[head+3]] = test_codelist[test_codelist[head+1]] * test_codelist[test_codelist[head+2]]
        head += 4
    return test_codelist[0]

for x in range(100):
    for y in range(100):
        if run_computer(x,y) == 19690720:
            print("Noun = " + str(x) + ", Verb = " + str(y) + ", Answer = " + str(100 * x + y))
            break

# Answer = 7264

