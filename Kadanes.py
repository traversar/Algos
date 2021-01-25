def kadanesAlgorithm(array):
    currMax = array[0]
    finalMax = array[0]
    for i in range(1, len(array)):
        num = array[i]
        currMax = max(num, currMax + num)
        finalMax = max(finalMax, currMax)
    return finalMax
