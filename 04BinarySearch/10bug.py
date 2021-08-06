#백준 - 3020 개똥벌레
#직선 구간 지나며 장애물 파괴. 최소 장애물 수와 그러한 구간의 수?
#n번째 구간은 길이가 n-1인 석순과  n인 석순의 중간 지점(n.5)
#mid보다 큰 석순의 개수+(h-mid)보다 큰 종유석의 개수
from sys import stdin
input=stdin.readline
n,h=map(int, input().rsplit()) #동굴의 길이, 높이
u,d=[0]*(h+1),[0]*(h+1) #종유석,석순
for i in range(n):#장애물의 크기
    if i%2==0:
        d[int(input())]+=1 #인덱스 높이로 날면 부딪치는 석순의 개수
    else:
        u[int(input())]+=1 #종유석
for i in range(h-1,0,-1): #마지막부터
    d[i]+=d[i+1]  #다음 길이에 해당 길이 포함되어 있음
    u[i]+=u[i+1]

min,count=n,0  #파괴하는 장애물 개수, 그러한 구간 수
#모든 비행높이에 대해 탐색해야함=>모든 석순과 종유석에 대해 반복문 돌리면 시간초과
#>> 각 높이로 비행했을 때 걸리는 장애물 개수 배열
for i in range(1,h+1):#비행높이가 석순:i보다 작고 종유석:h-i보다 커야함
    if min>(d[i]+u[h-i+1]):#더 작은 게 나오면 min갱신
        min=(d[i]+u[h-i+1])
        count=1
    elif min==(d[i]+u[h-i+1]):
        count+=1

print(min,count)
        



