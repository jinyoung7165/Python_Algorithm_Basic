#백준 1300 - K번째 수
#NxN 배열 A. A[i][j] = ixj 이 수를 일차원 배열 B에 넣으면 B의크기는 NxN이 됨
#B를 오름차순으로 정렬했을 때, B[k]?
from sys import stdin
input = stdin.readline
n = int(input())
k = int(input())
#각 행에서 임의의 a보다 작거나 같은 수의 개수를 구하는 식: a/행번호
def bs():
    result = 0
    left, right = 1, k #k번째 수의 가능한 최대 최소
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for i in range(1, n+1): #각 행 돌면서 해당하는 mid보다 같거나 작은 수의 개수 구함
            count += min(mid//i, n)

        if count >= k:
            #mid는 사실 배열 안에 존재하지 않지만 그것보다 작은 수들의 개수는 구할 수 있음 -> count == k일 때도 배열 안에서 mid보다 같거나 작은 수의 개수가 k개인 mid의 최솟값을 찾아야함
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
print(bs())