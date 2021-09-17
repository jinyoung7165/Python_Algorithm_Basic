#백준 1697 - 숨바꼭질
#A는 점 N, B는 점 K에 있음
#A가 N-1또는 N+1 또는 2*N 으로 1초 후에 이동 가능
#B를 찾을 수 있는 가장 빠른 시간은 몇 초 후인가?
#n,k주어짐 5 17=> 답: 4
#k를 2로 나눈 뒤 -1/+1 작업
from sys import stdin
from collections import deque
input=stdin.readline
n,k=map(int,input().split())
visited=[0]*(100001)

def bfs(n,k):
    count=0 #걸린 시간
    que=deque([[n,count]]) 
    while que: #큐가 빌 때까지 반복
        v,c=que.popleft() #맨 앞에서 원소 뽑아 출력
        if not visited[v]:
            visited[v]=True #현재 노드를 방문 처리
            if (v==k):#찾았다
                return c
            c+=1 #더 이동
            if v * 2 <= 100000:
                que.append([v * 2, c])
            if v + 1 <= 100000:
                que.append([v + 1, c])
            if v - 1 >= 0:
                que.append([v - 1, c])
    return c

print(bfs(n,k))