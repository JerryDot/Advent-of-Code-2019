with open('day8.txt', 'r') as text_input:
    input_string = text_input.read()

layers = []
while input_string:
    layers.append(input_string[:150])
    input_string = input_string[150:]

tally = [ [layer.count('0'), layer.count('1'), layer.count('2'), layer] for layer in layers]
for i, x in enumerate(tally):
    x.append(i)

min_zeros = 100
min_layer = 0
for row in tally:
    if row[0] < min_zeros:
        min_zeros = row[0]
        min_layer = row[-1] 

answer = tally[min_layer][1] * tally[min_layer][2]
print(answer)

# Answer = 2975