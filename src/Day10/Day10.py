
#inputLenghts = 3, 4, 1, 5
inputLenghts = 94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243

#values = list(range(0, 5))
values = list(range(0, 256))
valuesLength = len(values)

currentPosition = 0
skipSize = 0

def createSublist(length):
    subList = []
    for i in range(0, length):
        valuesPosition = i + currentPosition;
        if valuesPosition < valuesLength:
            subList.append(values[valuesPosition])
        elif valuesPosition >= valuesLength:
            subList.append(values[valuesPosition - valuesLength])
    return subList

def insertSublist(subList):
    for i in range(0, len(subList)):
        valuesI = i + currentPosition
        if valuesI < valuesLength:
            values[valuesI] = subList[i]
        elif valuesI >= valuesLength:
            values[valuesI - valuesLength] = subList[i]

for length in inputLenghts:
    if length > 1:
        subList = createSublist(length)
        subList.reverse()
        insertSublist(subList)
    currentPosition += length + skipSize
    if currentPosition >= valuesLength:
        currentPosition -= valuesLength
    skipSize += 1
print('Final list result: ', values)
print('Element 1: ', values[0], ' Element 2: ', values[1], ' Mulitplied they are: ', values[0] * values[1])
