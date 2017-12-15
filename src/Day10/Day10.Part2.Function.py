
def convert_input(input):
    conv_input = []
    [conv_input.append(ord(c)) for c in input]
    return conv_input

def createSublist(length):
    global values
    subList = []
    for i in range(length):
        valuesPosition = i + currentPosition;
        if valuesPosition < valuesLength:
            subList.append(values[valuesPosition])
        elif valuesPosition >= valuesLength:
            subList.append(values[valuesPosition - valuesLength])
    return subList

def insertSublist(subList):
    global values
    for i in range(len(subList)):
        valuesI = i + currentPosition
        if valuesI < valuesLength:
            values[valuesI] = subList[i]
        elif valuesI >= valuesLength:
            values[valuesI - valuesLength] = subList[i]

def convertSparseToDense():
    global values
    dense = []
    for i in range(16):
        min = i * 16
        max = (i + 1) * 16
        rangeResult = 0
        for v in values[min:max]:
            rangeResult ^= v
        dense.append(rangeResult)
    return dense

def convertDenseToHex(dense):
    global values
    hexResult = ''
    for value in dense:
        hexV = hex(value).split('x')[1];
        if len(hexV) == 1:
            hexV = '0' + hexV
        hexResult += hexV
    return hexResult

def get_knot_hex_hash_for_input(input):
    global currentPosition, skipSize, values, valuesLength

    values = list(range(0, 256))
    valuesLength = len(values)

    currentPosition = 0
    skipSize = 0

    # Convert input
    converted_input = convert_input(input)

    # Add assingment input
    converted_input += [17, 31, 73, 47, 23]

    # Start the loop
    for i in range(0, 64):
        for length in converted_input:
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

    # Convert Sparse Result to Dense result
    dense = convertSparseToDense()

    # Convert Dense Result to Hex and return it
    return convertDenseToHex(dense)