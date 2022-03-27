#백준 2470 - 두 용액
#산성: 1부터 양, 알칼리: -1부터 음
#서로 다른 용액을 혼합하여 0에 가까운 용액 만드는 두 용액의 특성 출력. 조합 여러 개면 아무거나 출력
from sys import stdin, maxsize
input = stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    left, right = 0, len(arr) - 1
    temp = maxsize
    while left < right:
        sum = arr[left] + arr[right]
        if temp > abs(sum):
            temp = abs(sum)
            result = [arr[left], arr[right]]
                
        if sum < 0:
            left += 1
        else:
            right -= 1

    return result

print(*solve())