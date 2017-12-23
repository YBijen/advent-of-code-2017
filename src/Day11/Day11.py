import io
import math

inp = open('input.txt').read()
pos = [0, 0, 0]

global f
f = 0

posNw = [-1, 0, 1]
posN = [-1, 1, 0]
posNe = [0, 1, -1]
posSe = [1, 0, -1]
posSw = [0, -1, 1]
posS = [1, -1, 0]

def repl_in_list(l):
	pos[0] += l[0]
	pos[1] += l[1]
	pos[2] += l[2]

def calc_distance():
	global f
	d = max(abs(pos[0]), abs(0 - pos[1]), abs(0 - pos[2]))
	if d > f:
		f = d
	return d

for dir in inp.split(','):
	if dir == 'nw':
		repl_in_list(posNw)
	elif dir == 'n':
		repl_in_list(posN)
	elif dir == 'ne':
		repl_in_list(posNe)
	elif dir == 'sw':
		repl_in_list(posSw)
	elif dir == 's':
		repl_in_list(posS)
	elif dir == 'se':
		repl_in_list(posSe)
	calc_distance()

print('X: ', pos[0])
print('Y: ', pos[1])
print('Z: ', pos[2])
print('The required steps to take and find the item at the given input is: ', calc_distance())
print('The furthest away he ever was, was', f, 'steps.')

# inefficient calculation below
#origPos = pos.copy();
#global steps
#steps = 0
#def clcStps():
#    global steps
#    while pos != [0, 0, 0]:
#        ih = pos.index(max(pos))
#        il = pos.index(min(pos))
#        if ih == 0 and il == 1:
#            repl_in_list(posN)
#        elif ih == 0 and il == 2:
#            repl_in_list(posNw)
#        elif ih == 1 and il == 0:
#            repl_in_list(posS)
#        elif ih == 1 and il == 2:
#            repl_in_list(posSw)
#        elif ih == 2 and il == 0:
#            repl_in_list(posSe)
#        elif ih == 2 and il == 1:
#            repl_in_list(posNe)
#        steps += 1