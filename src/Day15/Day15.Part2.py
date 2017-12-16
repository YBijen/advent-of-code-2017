
# Test input
start_a = 65
start_b = 8921

# Actual input
start_a = 699
start_b = 124

mod_value = 2147483647

amount_of_pairs = 5000000

equal_count = 0

def generator_a(value):
    global mod_value, amount_of_pairs
    pairs = []

    while len(pairs) < amount_of_pairs:
        value = (value * 16807) % mod_value
        if value % 4 == 0:
            pairs.append(value)
    return pairs

def generator_b(value):
    global mod_value, amount_of_pairs
    pairs = []

    while len(pairs) < amount_of_pairs:
        value = (value * 48271) % mod_value
        if value % 8 == 0:
            pairs.append(value)
    return pairs

print('Generator A running')
pairs_a = generator_a(start_a)
print('Generator B running')
pairs_b = generator_b(start_b)
print('Comparing...')
for i in range(amount_of_pairs):
   if str(format(pairs_a[i], 'b'))[-16:] == str(format(pairs_b[i], 'b'))[-16:]:
        equal_count += 1

print('Equal values:  ', equal_count)

