
import io

class Position:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

possible_dirs = {}
possible_dirs['N'] = [0,1]
possible_dirs['E'] = [1,0]
possible_dirs['S'] = [0,-1]
possible_dirs['W'] = [-1,0]

map_chars = ['+', '-', '|']
map = []

def print_pos_info(pos):
    print('Position {',pos.x, ',', pos.y, '} has value:', pos.value)

# Process Input
f=open("input.txt",'r')
for line in f.readlines():
    char_list = []
    for char in line.split('\n')[0]:
        char_list.append(Position(char, len(char_list), len(map)))
    map.append(char_list)
f.close()

length_map_x = len(map[0])
length_map_y = len(map)

def get_direction_moved_from(dir):
    if dir == 'N':
        return 'S'
    elif dir == 'E':
        return 'W'
    elif dir == 'S':
        return 'N'
    elif dir == 'W':
        return 'E'

def get_pos_at_direction(current_pos, direction):
        x = current_pos.x + direction[1][0]
        y = current_pos.y - direction[1][1]

        if x >= length_map_x or y >= length_map_y:
            return None

        return map[y][x]

def remove_invalid_directions(current_pos, directions):
    valid_dirs = {}
    for dir in directions.items():
        pos = get_pos_at_direction(current_pos, dir)

        if pos == None or pos.value == ' ':
            continue

        valid_dirs[dir[0]] = dir[1]

    return valid_dirs

def get_next_directions(next_prio_direction):
    next_directions = possible_dirs.copy()
    del next_directions[get_direction_moved_from(next_prio_direction)]
    return next_directions

# Configure the global variables used in the maze walk
characters = []
steps = 0
end_of_maze = False
next_pos = None
next_directions = {}
next_prio_direction = ''

# Configure the starting variable values
next_prio_direction = 'S'
next_directions = get_next_directions(next_prio_direction)

next_pos = next((p for p in map[0] if p.value != ' '), None) or next((p[0] for p in map if p[0].value != ' '), None)
print_pos_info(next_pos)

def walk_through_maze(current_pos, directions, prio_direction):
    global end_of_maze, next_pos, next_directions, next_prio_direction, characters, steps

    # Increase the step counter
    steps += 1

    # Start by processing the value of the current position
    if current_pos.value not in map_chars:
        characters.append(current_pos.value)

    directions = remove_invalid_directions(current_pos, directions)

    # Check if we're at the end
    if len(directions) == 0:
        end_of_maze = True
        return
    
    if len(directions) > 1:
        direction = list(directions.items())[list(directions.keys()).index(prio_direction)]
    else:
        direction = list(directions.items())[0]

    next_pos = get_pos_at_direction(current_pos, direction)
    next_prio_direction = direction[0]
    next_directions = get_next_directions(next_prio_direction)

while not end_of_maze:
    walk_through_maze(next_pos, next_directions, next_prio_direction)

print('While walking through the maze the following characters were found: ', ''.join(characters))
print('It did it in amount of steps: ', steps)