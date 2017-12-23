
import io

inp = open('input.txt').readlines()
#inp = ['0 <-> 2', '1 <-> 1', '2 <-> 0, 3, 4', '3 <-> 2, 4', '4 <-> 2, 3, 6', '5 <-> 6', '6 <-> 4, 5']

cnct_value = 0

total_values = []
values = []

def gt_idx_inp(v):
    idx = 0
    for l in inp:
        vl = int(l.split('<->')[0].strip())
        if v == vl:
            return idx
        idx += 1

def is_cnct_0(i, prI):
    idx = int(inp[gt_idx_inp(i)].split('<->')[0].strip())
    cnts = [int(c.strip()) for c in inp[gt_idx_inp(i)].split('<->')[1].strip().split(',')]

    # Delete the Previous value from the possible connections
    cnts.pop(cnts.index(prI))

    if len(cnts) < 1:
        return False
    elif cnct_value in cnts:
        return True
    else:
        return any(c in values or is_cnct_0(c, idx) for c in cnts)


toPop = []

while(len(inp) > 0):
    if(len(toPop) > 0):
        toPop.reverse()
    [inp.pop(list.index(gt_idx_inp(x))) for x in toPop]
    toPop = []
    cnct_value = int(inp[0].split('<->')[0].strip())
    values = []
    for l in inp:
        idx = int(l.split('<->')[0].strip())
        cnts = [int(c.strip()) for c in l.split('<->')[1].strip().split(',')]
    
        print('Current loop: ', idx)

        if idx in inp:
            continue

        if idx == cnct_value:
            values.append(idx)
            toPop.append(idx)
            for c in cnts:
                values.append(c)
                toPop.append(c)
        elif cnct_value in cnts:
            values.append(idx)
            toPop.append(idx)
        else:
            if any(is_cnct_0(c, idx) for c in cnts):
                values.append(idx)
                toPop.append(idx)
    total_values.append(values)


print('Input: ', inp)
print('The values connected to 0 are: ', set(values))
print('The length of values: ', len(set(values)))
