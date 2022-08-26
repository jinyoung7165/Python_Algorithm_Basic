#회의실 배정
#1개의 회의실을 n개의 회의가 사용
#각 회의는 시작-끝 시간이 있음, 겹치지 않게 사용 회의 최대 개수
#회의가 끝나는 동시에 다음 회의가 시작할 수 있음
#시작과 동시에 끝나는 회의 존재 가능
#가장 빨리 끝나는 회의부터 넣어야 많이 넣을 수 있음
#가장 빨리 끝 - 가장 빨리 시작 관계는 회의실 전체 개수 볼 때 사용
from sys import stdin
input = stdin.readline
graph = []
n = int(input())
for i in range(n):
    graph.append(list(map(int,input().split()))) #시작,끝시간

graph.sort(key = lambda x: (x[1], x[0])) #끝나는 시간부터 정렬

cnt = 1
end_time = graph[0][1]
for i in range(1, n):
    if graph[i][0] >= end_time:
        cnt+=1
        end_time = graph[i][1]

print(cnt)
