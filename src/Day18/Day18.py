
import io

instructions = open('input.txt').readlines()
#instructions = open('test_input.txt').readlines()

registers = {}
last_sound = 0
recovered_sound = 0
idx = 0

# Register all "x-keys" for a cleaner main function :)
for instruction in instructions:
    x_key = instruction.split()[1]
    if registers.get(x_key) == None:
        registers[x_key] = 0

while recovered_sound == 0:
    #print('Current values: ', registers)
    parts = instructions[idx].split()

    # assign variables
    action = parts[0]

    x_key = parts[1]
    x_value = registers[x_key]

    if len(parts) > 2:
        y_key = parts[2]
        try:
            y_value = int(y_key)
        except ValueError:
            y_value = registers[y_key]

    if action == 'snd':
        last_sound = x_value
        #print('Setting last_sound to: ', x_value)
    elif action == 'set':
        registers[x_key] = y_value
        #print('Setting', x_key, ' to: ', y_value)
    elif action == 'add':
        registers[x_key] += y_value
        #print('Adding value of ', x_key, '[', x_value, '] to: ', y_value)
    elif action == 'mul':
        registers[x_key] = x_value * y_value
        #print('Multiplying value of ', x_key, '[', x_value, '] to: ', y_value)
    elif action == 'mod':
        registers[x_key] = x_value % y_value
        #print('Modulo value of ', x_key, '[', x_value, '] to: ', y_value)
    elif action == 'jgz' and x_value > 0:
        idx += y_value - 1
        #print('Changed index to: ', idx)
    elif action == 'rcv' and x_value != 0:
        recovered_sound = last_sound
        #print('Recovered the sound to:', recovered_sound)

    idx += 1

print('The recovered sound is: ', recovered_sound)