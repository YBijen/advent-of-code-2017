
input = 354
max_idx = 50000000

interval = 1000000
insert_idx = 0
value_at_index_1 = 0
state_length = 1

for idx in range(1, max_idx+1):
    if idx % interval == 0:
        print('Current: ', idx, ' loops left: ', max_idx - idx)
    insert_idx = ((insert_idx + input) % state_length) + 1
    state_length += 1
    if insert_idx == 1:
        value_at_index_1 = idx

print('Value of item after 0: ', value_at_index_1)