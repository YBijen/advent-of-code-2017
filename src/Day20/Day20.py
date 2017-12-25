
import io

def convert_str_to_tuple(str):
    numbers = str.split('<')[1].split('>')[0].split(',')
    return (int(numbers[0]), int(numbers[1]), int(numbers[2]))

def calc_distance(pos):
    return abs(pos[0] + pos[1] + pos[2])

closest_to_0 = None
slowest_moving = None

idx = 0
f=open("input.txt",'r')
for line in f.readlines():
    particle = line.split('\n')[0].split()

    pos = convert_str_to_tuple(particle[0])
    vel = convert_str_to_tuple(particle[1])
    acc = convert_str_to_tuple(particle[2])

    start = calc_distance(pos)

    if closest_to_0 == None or start <= closest_to_0[1]:
        print('Changing closest to 0 from: --', closest_to_0, '-- to ==', (idx, start), '==')
        closest_to_0 = (idx, start)

    # Increase the X/Y/Z velocity by the X/Y/Z acceleration
    vel = (vel[0] + acc[0], vel[1] + acc[1], vel[2] + acc[2])
    # Increase the X/Y/Z position by the X/Y/Z velocity
    pos = (pos[0] + vel[0], pos[1] + vel[1], pos[2] + vel[2])

    end = calc_distance(pos)

    diff = end - start

    if slowest_moving == None or diff <= slowest_moving[1]:
        print('Changing slowest moving from: --', slowest_moving, '-- to ==', (idx, diff), '==')
        slowest_moving = (idx, diff)

    idx += 1
f.close()

print('=== Result ===')
print('Closest: ', closest_to_0)
print('Slowest: ', slowest_moving)


# Calculate the starting distance
# Calculate the finishing distance
# Lowest result of finish - start is the winner
