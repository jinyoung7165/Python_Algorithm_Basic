import heapq
#0082663 input
def getLargestNumber(num):
    # Write your code here
    arr = list(map(int,list(num)))
    stack, result = [], []
    for i, num in enumerate(arr):
        if not stack or num % 2 == arr[i-1] % 2:
            heapq.heappush(stack, (-num, num))
        elif num % 2 != arr[i-1] % 2:
            while stack:
                result.append(str(heapq.heappop(stack)[1]))
            heapq.heappush(stack, (-num, num))
    
    while stack:
        result.append(str(heapq.heappop(stack)[1]))
        
    resultString= ''.join(result)
    return resultString
if __name__ == '__main__':
   
    num = input()

    result = getLargestNumber(num)

    print(result)