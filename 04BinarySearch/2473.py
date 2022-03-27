#백준 2473 - 세 용액
#세 개 섞어서 가장 0에 가까운 용액
import sys
input = sys.stdin.readline
#i, j(left), k(right)
def bs():
    n = int(input())
    arr = [int(x) for x in input().split()] #시간절약!!!!!!!
    #arr = list(map(int, input().split()))
    arr.sort()
    result = [0] * 3
    temp = sys.maxsize
    for i in range(n-2):
        if i > 0 and arr[i] == arr[i -1]:
            continue #어차피 같은 조합만 만들어짐
        left, right = i+1, n-1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if temp > abs(sum):
                temp = abs(sum)
                result[0], result[1], result[2] = arr[i], arr[left], arr[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                print(arr[i], arr[left], arr[right])
                exit()
    return result
print(*bs())