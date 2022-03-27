#백준 10816-숫자카드2
#카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 카드를 몇 개 가지고 있는지
from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

def bs(arr, target):
    right_idx = bisect_right(arr, target)
    left_idx = bisect_left(arr, target)
    return right_idx - left_idx

def count_card():
    m = int(input())
    M = list(map(int, input().split())) #숫자카드
    n = int(input())
    N = list(map(int, input().split())) #주어진 수
    M.sort()#탐색을 위한 정렬
    
    result = []
    for num in N:
        result.append(bs(M, num))
    print(*result)

count_card()


