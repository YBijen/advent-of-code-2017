
programs = list('abcde')
programs = list('abcdefghijklmnop')

starting_programs =  'abcdefghijklmnop'

# Test Moves
moves = ['s1', 'x3/4', 'pe/b']
moves = [l for l in open('input.txt').readline().split(',')]

find_repetition_tries = 100
max_dances = 1000000000

def perform_spin(spin):
    global programs
    current_order = programs.copy()
    spin_value = int(spin.split('s')[1])
    for i in range(len(programs)):
        new_i = (i + spin_value) % len(programs)
        programs[new_i] = current_order[i]

def perform_exchange(exchange):
    global programs
    prgrm_1 = int(exchange[1:].split('/')[0])
    prgrm_2 = int(exchange[1:].split('/')[1])

    temp = programs[prgrm_1]
    programs[prgrm_1] = programs[prgrm_2]
    programs[prgrm_2] = temp

def perform_partner_swap(partner_swap):
    global programs
    value_partner_1 = partner_swap[1:].split('/')[0]
    idx_partner_1 = programs.index(value_partner_1)

    value_partner_2 = partner_swap[1:].split('/')[1]
    idx_partner_2 = programs.index(value_partner_2)

    programs[idx_partner_1] = value_partner_2
    programs[idx_partner_2] = value_partner_1

def print_list(list):
    return ''.join(l for l in list)

def perform_moves(moves):
    for move in moves:
        if move[0] == 's':
            perform_spin(move)
        if move[0] == 'x':
            perform_exchange(move)
        elif move[0] == 'p':
            perform_partner_swap(move)

def perform_dance(dances, moves):
    global programs
    for dance in range(dances):
        if dance > 0 and starting_programs == print_list(programs):
            return dance
        perform_moves(moves)

def get_first_repetition(dances, moves):
    global programs
    for dance in range(dances):
        if dance > 0 and starting_programs == print_list(programs):
            return dance
        perform_moves(moves)
    return -1

print('Calculating the amount of dances required before finding our starting position again...')
required_repetitions = get_first_repetition(find_repetition_tries, moves)
if required_repetitions == -1:
    print('Could not find the required repetitions before dance', find_repetition_tries, '. Increase that number or fix the bug :)')
else:
    dances = max_dances % required_repetitions
    print('Starting the dance. This dance will perform:', dances, 'times')
    print('Starting position: ', print_list(programs))
    perform_dance(dances, moves);
    print('Finishing position: ', print_list(programs))