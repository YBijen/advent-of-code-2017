
import io

# Process Input
instructions = []
file_name = 'test_input.txt'
file_name = 'input.txt'
f=open(file_name,'r')
for line in f.readlines():
    instructions.append(line.split('\n')[0])
f.close()

registers = [{}, {}]
queues = [[], []]
idx = [0, 0]
status = ['ok', 'ok']

values_sent = 0

# Register all "x-keys" for a cleaner main function :)
for instruction in instructions:
    x_key = instruction.split()[1]
    if registers[0].get(x_key) == None:
        try:
            int(x_key)
        except ValueError:
            registers[0][x_key] = 0
    if registers[1].get(x_key) == None:
        try:
            int(x_key)
        except ValueError:
            value = 0
            if x_key == 'p':
                value = 1
            registers[1][x_key] = value

def get_value(i, key):
    try:
        return int(key)
    except ValueError:
        return registers[i][key]

loops = 0

def process_instructions(program_index):
    global values_sent, loops
    while status[program_index] == 'ok':        
        loops += 1
        parts = instructions[idx[program_index]].split()

        # assign variables for readability
        action = parts[0]
        x_key = parts[1]
        x_value = get_value(program_index, x_key)
        if len(parts) > 2:
            y_key = parts[2]
            y_value = get_value(program_index, y_key)

        if action == 'snd':
            other_index = 0
            if program_index == 0:
                other_index = 1
            queues[other_index].append(x_value)
            status[other_index] = 'ok'
            if program_index == 1:
                values_sent += 1
        elif action == 'set':
            registers[program_index][x_key] = y_value
        elif action == 'add':
            registers[program_index][x_key] += y_value
        elif action == 'mul':
            registers[program_index][x_key] *= y_value
        elif action == 'mod':
            registers[program_index][x_key] %= y_value
        elif action == 'jgz' and x_value > 0:
            idx[program_index] += y_value - 1
        elif action == 'rcv':
            if len(queues[program_index]) > 0:
                registers[program_index][x_key] = queues[program_index][0]
                queues[program_index].pop(0)
            else:
                status[program_index] = 'waiting'

        if status[program_index] == 'ok':
            idx[program_index] += 1

        if idx[program_index] >= len(instructions) or idx[program_index] < 0:
            status[program_index] = 'done'


while status[0] == 'ok' or status[1] == 'ok':
    print('Current values esnt: ', values_sent)
    if status[0] != 'ok' and status[1] != 'ok':
        print('Both not ok')
    if status[0] == 'ok':
        process_instructions(0)
    if status[1] == 'ok':
        process_instructions(1)

print('Program 1 send this amount of values: ', values_sent)