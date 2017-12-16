
# Test input
start_a = 65
start_b = 8921

# Actual input
start_a = 699
start_b = 124

factor_a = 16807
factor_b = 48271

mod_value = 2147483647

pairs = 40000000

equal_count = 0


def generate_value(value, factor, mod_value):
    return (value * factor) % mod_value


current_a = start_a
current_b = start_b

print('Generator Running')
for i in range(pairs):
    if i % 1000000 == 0:
        print('Iteration: ', i)

    current_a = generate_value(current_a, factor_a, mod_value)
    current_b = generate_value(current_b, factor_b, mod_value)

    str_a = str(format(current_a, 'b'))[-16:]
    str_b = str(format(current_b, 'b'))[-16:]

    if str_a == str_b:
        equal_count += 1

print('Equal values:  ', equal_count)

