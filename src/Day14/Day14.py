
# Obtain the Knot Hash Hex calculation function
filename = '..\\Day10\\Day10.Part2.Function.py'
exec(open(filename).read())

total_used_squares = 0

def convert_hex_to_binary(hex_str):
    return format(int(hex_str, 16), '0>128b')

def count_char_in_str(str, char):
    return str.count(char)

base_input = 'jzgqcdpd-'
#base_input = 'flqrgnkx-'
for i in range(128):
    #print('Loop: ', i)
    hex_str = get_knot_hex_hash_for_input(base_input + str(i))
    bin_str = convert_hex_to_binary(hex_str)
    total_used_squares += count_char_in_str(bin_str, '1')

print('Base input: ', base_input)
print('Total amount of used squares: ', total_used_squares)
