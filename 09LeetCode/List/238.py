#자신을 제외한 배열의 곱
#배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력
#입력: [1,2,3,4]
#출력: [24,12,8,6]
#나눗셈하지 않고 O(n)에 풀이하라
#자신 제외, 왼쪽 오른쪽 부분의 곱
def multiply(arr = [1,2,3,4]):
    left = []
    temp = 1
    for i in range(len(arr)):
        left.append(temp) #이전 원소까지의 곱
        temp *= arr[i]
        
    temp = 1 #맨 오른쪽 자기자신을 뺀 오른쪽 부분의 곱
    for i in range(len(arr)-1, -1, -1): #왼쪽부분에 오른쪽 부분의 곱
        left[i] *= temp
        temp *= arr[i] #현재 자신을 곱함   
    
    return left

print(multiply())