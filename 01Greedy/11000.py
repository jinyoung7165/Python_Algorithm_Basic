#강의실 배정
#si에 시작해서 ti에 끝나는 n개의 수업
#최소의 강의실을 사용해 모든 수업
from sys import stdin
import heapq
input = stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

arr.sort(key = lambda x :  x[0]) #빨리 시작하는 강의 순

end_time = [] #각 강의실 별 끝나는 시간
heapq.heappush(end_time, arr[0][1])

for i in arr[1:]:
    if i[0] >= end_time[0]: #가장 빨리 끝나는 시간보다 가장 빨리 시작하는 시간이 뒤면
        heapq.heappop(end_time) #같은 강의실 사용 가능
        heapq.heappush(end_time, i[1])
    else:
        heapq.heappush(end_time, i[1]) #다른 강의실 사용
    
print(len(end_time))