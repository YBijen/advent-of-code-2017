import io;

def CheckAndOrCreateKey(key):
	if(dict.get(key) == None):
		dict[key] = 0;

def IsMatch(splLine):
	if(splLine[1] == '<'):
		return dict.get(splLine[0]) < int(splLine[2])
	elif(splLine[1] == '>'):
		return dict.get(splLine[0]) > int(splLine[2])
	elif(splLine[1] == '=='):
		return dict.get(splLine[0]) == int(splLine[2])
	elif(splLine[1] == '>='):
		return dict.get(splLine[0]) >= int(splLine[2])
	elif(splLine[1] == '<='):
		return dict.get(splLine[0]) <= int(splLine[2])
	elif(splLine[1] == '!='):
		return dict.get(splLine[0]) != int(splLine[2])
	else:
		print('Couldnt find out what to do with: ', splLine[1])
		raise

with open("input.txt") as txt:
	dict = {}
	for line in txt:
		splLine = line.split('if')[1].strip().split();
		CheckAndOrCreateKey(splLine[0])
		if(IsMatch(splLine)):
			splLine = line.split('if')[0].strip().split();
			CheckAndOrCreateKey(splLine[0])
			if(splLine[1] == 'inc'):
				dict[splLine[0]] = dict.get(splLine[0]) + int(splLine[2])
			else: # then decrease
				dict[splLine[0]] = dict.get(splLine[0]) - int(splLine[2])
	txt.close()
	highest = 0;
	for value in dict:
		if(int(dict[value]) > highest): highest = int(dict[value])

	print('The highest number is: ', highest)


