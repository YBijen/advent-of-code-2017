import io;

highestValue = 0;

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
			# Below is for part 2
			if(int(dict.get(splLine[0])) > highestValue): highestValue = int(dict.get(splLine[0]))
	txt.close()

	# Below was for part 1
	#for value in dict:
	#	if(int(dict[value]) > highestValue): highestValue = int(dict[value])

	print('The highest number is: ', highestValue)


