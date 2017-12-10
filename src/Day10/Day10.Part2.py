
#inputLengths = '1,2,3'
inputLengths = '94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243'
convertedInput = []
dense = []
global hexResult;
hexResult = ''

print('Input: ', inputLengths)

#values = list(range(0, 5))
values = list(range(0, 256))
valuesLength = len(values)

currentPosition = 0
skipSize = 0

def createSublist(length):
    subList = []
    for i in range(length):
        valuesPosition = i + currentPosition;
        if valuesPosition < valuesLength:
            subList.append(values[valuesPosition])
        elif valuesPosition >= valuesLength:
            subList.append(values[valuesPosition - valuesLength])
    return subList

def insertSublist(subList):
    for i in range(len(subList)):
        valuesI = i + currentPosition
        if valuesI < valuesLength:
            values[valuesI] = subList[i]
        elif valuesI >= valuesLength:
            values[valuesI - valuesLength] = subList[i]

def convertInput():
    for char in inputLengths:
        convertedInput.append(ord(char))

def convertSparseToDense():
    for i in range(16):
        min = i * 16
        max = (i + 1) * 16
        rangeResult = 0
        for v in values[min:max]:
            rangeResult ^= v
        dense.append(rangeResult)

def convertDenseToHex():
    global hexResult
    for value in dense:
        hexV = hex(value).split('x')[1];
        if len(hexV) == 1:
            hexV = '0' + hexV
        hexResult += hexV

# Start with converting input
convertInput()

# Add assingment input
convertedInput += [17, 31, 73, 47, 23]

# Start the loop
for i in range(0, 64):
    for length in convertedInput:
        if length > 1:
            subList = createSublist(length)
            subList.reverse()
            insertSublist(subList)
        currentPosition += length + skipSize
        if currentPosition >= valuesLength:
            currentPosition %= valuesLength
        skipSize += 1
        if skipSize >= valuesLength:
            skipSize = 0

convertSparseToDense()
print('Dense values: ', dense)
convertDenseToHex()

print('Final Hex Result is: ', hexResult)