
def compressWord(word, k):
    stack = []
    temp = '' #last character
    
    for i in list(word):
        if i == temp: #same as the last one
            count = stack.pop()[1] + 1 # consecutive 
            if count != k:
                stack.append([i, count])
            else:
                if stack:
                    temp = stack[-1][0]
                else:
                    temp = ''
        else:
            stack.append([i, 1])
            temp = i
    
    result = ''
    for i in stack:
        result += i[0] * i[1]
    return result
print(compressWord('aabbccca', 3))