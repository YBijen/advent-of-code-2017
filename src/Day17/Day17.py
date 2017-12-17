
input = 354
max_idx = 2017

# Test input
#input = 3
#max_idx = 4

state = [0]
insert_idx = 0

for idx in range(1, max_idx+1):
    insert_idx = ((insert_idx + input) % (len(state))) + 1
    state.insert(insert_idx, idx)


#print('Result: ', state)
print('Given input: ', input)
print('Index of given input: ', state.index(max_idx))
print('Value of item of input.index + 1: ', state[state.index(max_idx) + 1])