
import io

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Position:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

possible_dirs = [Coord(0, 1), Coord(1, 0), Coord(0, -1), Coord(-1, 0)]

map_chars = ['+', '-', '|']
map = []

# Process Input
f=open("input.txt",'r')
lines = f.readlines()
max_length_lines = len(lines) - 1
for idx in range(0, len(lines)):
    y = (max_length_lines - idx)
    line = lines[y].split('\n')[0]
    char_list = []
    for char in line:
        char_list.append(Position(char, len(char_list), y))
    map.append(char_list)
f.close()

def calc_y(current_y):
    return max_length_lines - current_y

length_map_x = len(map[0])
length_map_y = len(map)

def get_start_pos():
    start_pos = next((p for p in map[(len(map) - 1)] if p.value != ' '), None)
    if start_pos == None:
        start_pos = next((p[0] for p in map if p[0].value != ' '), None)
    return start_pos

def get_previous_direction(current_pos, previous_pos):
    return Coord(current_pos.x - previous_pos.x, current_pos.y - previous_pos.y)

def get_pos_at_dir(current_pos, dir):
    x_value = current_pos.x + dir.x
    y_value = calc_y(current_pos.y + dir.y)

    if x_value >= length_map_x or y_value >= length_map_y:
        return None

    return map[y_value][x_value]

def get_index_coord(possible_dirs, coord):
    idx = 0
    for p_dir in possible_dirs:
        if p_dir.x == coord.x and p_dir.y == coord.y:
            return idx
        else:
            idx += 1

def is_next_pos_valid(pos):
    if pos.value == ' ':
        return False
    elif pos.value not in map_chars:
        result_list.append(next_pos.value)
    return True

def get_next_pos(current_pos, previous_pos):
    direction = get_previous_direction(previous_pos, current_pos)
    
    print('Current direction: ', direction.x, direction.y)
    print('Current Position: ', current_pos.x, current_pos.y, 'Value: ', current_pos.value)

    # Check if pos at next value in the same direction is correct
    next_pos = get_pos_at_dir(current_pos, direction)

    if is_next_pos_valid(next_pos):
        return next_pos

    # Create a set of the 2 possible remaining directions
    current_possible_dirs = possible_dirs.copy()

    # Get the way it came from and remove that from possible directions
    current_possible_dirs.pop(get_index_coord(current_possible_dirs, get_previous_direction(current_pos, previous_pos)))

    # Remove the just checked way it came from
    current_possible_dirs.pop(get_index_coord(current_possible_dirs, direction))

    for dir in current_possible_dirs:
        pos_at_dir = get_pos_at_dir(current_pos, dir)
        if pos_at_dir == None or pos_at_dir.value == ' ':
            current_possible_dirs.pop(get_index_coord(current_possible_dirs, dir))
    if len(current_possible_dirs) == 0:
        return None
    if len(current_possible_dirs) > 1:
        for dir in current_possible_dirs:
            if not dir == direction:
                current_possible_dirs.pop(get_index_coord(current_possible_dirs, dir))
    next_pos = get_pos_at_dir(current_pos, current_possible_dirs[0])
    if is_next_pos_valid(next_pos):
        return next_pos

result_list = []
start_pos = get_start_pos()

print('Start X: ', start_pos.x)
print('Start Y: ', start_pos.y)

if start_pos.x == 0:
    previous_pos = Coord(start_pos.x-1, start_pos.y)
else:
    previous_pos = Coord(start_pos.x, start_pos.y+1)

print('Previous X: ', previous_pos.x)
print('Previous Y: ', previous_pos.y)
current_pos = start_pos

while current_pos != None:
    new_pos = get_next_pos(current_pos, previous_pos)
    previous_pos = current_pos
    current_pos = new_pos

print('Values found in order: ', result_list)
