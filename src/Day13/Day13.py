
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

# Create full list
for idx in range(0, max_idx):
    values[idx] = input_list.get(idx) or 0

def get_current_pos(picoSec):
    depth = (values[picoSec] - 1) * 2
    if depth <= 0:
        return -1
    elif depth > 0:
        return picoSec % depth

for picoSec in range(0, max_idx):
    if get_current_pos(picoSec) == 0:
        caught[picoSec] = values[picoSec]

for c in caught:
    total_severity += c * caught[c]

print('The total severity of the trip is: ', total_severity)

