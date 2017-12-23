
import io

inp = open('input.txt').readlines()
#inp = ['0 <-> 2', '1 <-> 1', '2 <-> 0, 3, 4', '3 <-> 2, 4', '4 <-> 2, 3, 6', '5 <-> 6', '6 <-> 4, 5']

values = []

def is_cnct_0(i, prI):
    idx = int(inp[i].split('<->')[0].strip())
    cnts = [int(c.strip()) for c in inp[i].split('<->')[1].strip().split(',')]

    # Delete the Previous value from the possible connections
    cnts.pop(cnts.index(prI))

    if len(cnts) < 1:
        return False
    elif 0 in cnts:
        return True
    else:
        return any(c in values or is_cnct_0(c, idx) for c in cnts)

for l in inp:
    idx = int(l.split('<->')[0].strip())
    cnts = [int(c.strip()) for c in l.split('<->')[1].strip().split(',')]
    
    print('Current loop: ', idx)

    if idx in inp:
        continue

    if idx == 0:
        values.append(idx)
        for c in cnts:
            values.append(c)
    elif 0 in cnts:
        values.append(idx)
    else:
        if any(is_cnct_0(c, idx) for c in cnts):
            values.append(idx)


print('Input: ', inp)
print('The values connected to 0 are: ', set(values))
print('The length of values: ', len(set(values)))
