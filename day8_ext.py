with open('day8.txt', 'r') as text_input:
    input_string = text_input.read()

layers = []
while input_string:
    layers.append(input_string[:150])
    input_string = input_string[150:]

tally = [ [int(d) for d in str(layer)] for layer in layers]
#print(tally)

for i, layer in enumerate(tally):
    for j, digit in enumerate(layer):
        if digit < 2 and i <99 :
            tally[i+1][j] = digit

print(tally[-1][0:24])
print(tally[-1][25:49]) 
print(tally[-1][50:74]) 
print(tally[-1][75:99]) 
print(tally[-1][100:124]) 
print(tally[-1][125:149]) 

"""
Answer spells: EHRUE
[1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1]
[1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0]
[1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0]
[1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0]
[1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0]
[1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1]
"""

