
import io

max_idx = 0
input_list = {}
values = {}
caught = {}
total_severity = 0

# Parse input
for line in open('input.txt').readlines():
    idx = int(line.split(':')[0])
    input_list[idx] = int(line.split(':')[1].strip())
    if idx > max_idx:
        max_idx = idx

#input_list = {}
#input_list[0] = 3
#input_list[1] = 2
#input_list[4] = 4
#input_list[6] = 4

# Create full list
for idx in range(0, max_idx):
    values[idx] = input_list.get(idx) or 0

def get_current_pos(picoSec):
    depth = (values[picoSec] - 1) * 2
    if depth <= 0:
        return -1
    elif depth > 0:
        return picoSec % depth

def is_pos_safe(range, picoSec):
    depth = (input_list.get(range) - 1) * 2
    if depth <= 0:
        return True
    elif depth > 0:
        return (picoSec % depth) != 0

for picoSec in range(0, max_idx):
    if get_current_pos(picoSec) == 0:
        caught[picoSec] = input_list[picoSec]

for c in caught:
    total_severity += c * caught[c]

searching = True
delay = 0;
while(searching):
    all_inp = True
    for inp in input_list:
        if not is_pos_safe(inp, delay + inp):
            all_inp = False
            break;
    if all_inp:
        searching = False
    else:
        delay += 1


print('The total severity of the trip is: ', total_severity)
print('The total required delay before passing safely is: ', delay)