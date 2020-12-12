def getEntries(arr, freq, keySum):
    for i in arr:
        complement = keySum - i
        if i == complement:
            continue
        elif complement in freq:
            return [i, complement]
    return []
        
def getFreq(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

def getEntries2(arr, freq, keySum):
    for i in arr:
        complement = keySum - i
        if i == complement:
            continue
        else:
            compNums = getEntries(arr, freq, complement)
        if len(compNums) == 2:
            return compNums + [i]

if __name__ == '__main__':
    file = open('input.txt', 'r')
    nums = []
    for i in file:
        nums.append(int(i))
    freq = getFreq(nums)
    values = getEntries(nums, freq, 2020)
    print("The two numbers in the list that add to 2020 are %d and %d" %(values[0], values[1]))
    print("The product is %d" %(values[0] * values[1]))
    
    #Part 2
    values = getEntries2(nums, freq, 2020)
    print("The three numbers in the list that add to 2020 are %d, %d, and %d" %(values[0], values[1], values[2]))
    print("The product is %d" %(values[0] * values[1] * values[2]))