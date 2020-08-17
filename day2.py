with open('day2.txt', 'r') as codestring:
    codelist = codestring.read().split(',')
    codelist = list(map(int, codelist))

#restore gravity assist program
codelist[1] = 12
codelist[2] = 2

head = 0
while codelist[head] != 99:
    print(codelist[head], head)
    if codelist[head] == 1:
        codelist[codelist[head+3]] = codelist[codelist[head+1]] + codelist[codelist[head+2]]
    if codelist[head] == 2:
        codelist[codelist[head+3]] = codelist[codelist[head+1]] * codelist[codelist[head+2]]
    head += 4

print(codelist[0])

# answer = 4138658