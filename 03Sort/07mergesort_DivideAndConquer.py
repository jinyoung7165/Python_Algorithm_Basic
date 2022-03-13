#백준 2751 - 수 정렬하기2
#N개의 수가 주어졌을 때, 오름차순으로 정렬
#merge_sort : 시간복잡도 O(NlogN), 공간:log(N)
#데이터를 절반씩 나눠 1개로 만들고(분할)
#다시 절반씩 합치면서 그 안에서 정렬(정복)
from sys import stdin
input = stdin.readline

def merge_sort(array):
    if len(array)<=1: #하나가 될 때까지
        return array
    mid = len(array) // 2 #나눔
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:]) #반쪼가리 씩 계속 반쪽으로 나눔

    arr = []
    l=r=0
    #왼쪽 배열과 오른쪽 배열의 최소끼리 비교
    while l<len(left) and r<len(right):
        if left[l]<right[r]: #왼쪽배열의 최소가 더 작을 때
            arr.append(left[l])
            l+=1 #다음 최소랑 오른쪽 최소랑 비교
        else: #오른쪽 배열의 최소가 더 작을 때
            arr.append(right[r])
            r+=1
    #left 또는 right 중 비교도 없이 남은 애들         
    if(l<len(left)): arr += left[l:]
    if(r<len(right)): arr += right[r:]
    return arr

# 데이터 입력
n=int(input())
num = []

for _ in range(n):
    num.append(int(input()))

result = merge_sort(num)

for i in result:
    print(i)