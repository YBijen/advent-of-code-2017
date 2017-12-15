
import collections
Coord = collections.namedtuple('Coord', ['x', 'y'])

# Obtain the Knot Hash Hex calculation function
filename = '..\\Day10\\Day10.Part2.Function.py'
exec(open(filename).read())

coords = []
group = []

# Key = Group index
# Value = Array of Coords
result = {}

current_index = 1

# Given Input
base_input = 'jzgqcdpd-'
# Example Input
#base_input = 'flqrgnkx-'

def convert_hex_to_binary(hex_str):
    return format(int(hex_str, 16), '0>128b')

for y in range(128):
    print('Loop: ', y)
    hex_str = get_knot_hex_hash_for_input(base_input + str(y))
    bin_str = convert_hex_to_binary(hex_str)
    for x in range(len(bin_str)):
        if bin_str[x] == '1':
            coords.append(Coord(x, y))

while len(coords) > 0:
    if len(group) > 0:
        result[current_index] = group.copy()
        current_index += 1
        group = []

    neighbours = [coords[0]]
    while len(neighbours) > 0:
        for c in neighbours:
            group.append(c)
            neighbours.pop(neighbours.index(c))
            coords.pop(coords.index(c))

            cn1 = Coord(c.x-1, c.y)
            cn2 = Coord(c.x, c.y+1)
            cn3 = Coord(c.x+1, c.y)
            cn4 = Coord(c.x, c.y-1)

            if cn1 in coords and cn1 not in neighbours:
                neighbours.append(cn1)
            if cn2 in coords and cn2 not in neighbours:
                neighbours.append(cn2)
            if cn3 in coords and cn3 not in neighbours:
                neighbours.append(cn3)
            if cn4 in coords and cn4 not in neighbours:
                neighbours.append(cn4)

print('Base input: ', base_input)
print('Highest Index: ', current_index)