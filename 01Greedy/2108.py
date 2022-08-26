#통계학
#n:홀수
#산술평균:n개 수의 합을 n으로 나눈 것
#중앙값:n개의 수를 증가순으로 나열 시 중앙
#최빈값:n개의 수 중 가장 많이 나타난 값(여러 개일 때 두번째로 작은값)
#범위:n개의 수 중 최대와 최소 차이
from collections  import Counter
from sys import stdin
input = stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
counter = Counter(arr).most_common(2)

print(round(sum(arr)/n))
print(arr[n//2]) #중앙값
if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print(counter[1][0])
else:
    print(counter[0][0])
    
print(arr[-1]- arr[0])