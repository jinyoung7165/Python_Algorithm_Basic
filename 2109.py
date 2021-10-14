#백준2109 - 순회강연
#n개 대학에서 강연요청. d일에 와서 강연을 하면 p만큼 돈
#벌 수 있는 가장 많은 돈은?
#같은 d의 p끼리 비교
from sys import stdin
import heapq
input=stdin.readline
n=int(input())
que=[]
for i in range(n):
    p,d=map(int,input().split())
    heapq.heappush(que,(d,-p)) #날짜순 p최대힙

sum,lastday=0,0
for i in range(n):
    d,p=heapq.heappop(que)
    #print(":",d,p)
    if(d!=lastday):sum+=-p
    lastday=d

print(sum)