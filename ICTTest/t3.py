#[[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]

def countPairs(numbers, k):
    # Write your code here
    result = 0
    numSet = set(numbers)
    for pair in numSet:
        if (pair + k) in numSet:
            result += 1
    return result
print(countPairs([7,3,2,3,4],1))