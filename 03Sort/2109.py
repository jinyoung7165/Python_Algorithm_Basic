#백준2109 - 순회강연
#n개 대학에서 강연요청. d일에 와서 강연을 하면 p만큼 돈
#벌 수 있는 가장 많은 돈은?
#같은 d의 p끼리 비교
from sys import stdin
import heapq
input=stdin.readline
n=int(input())
que,arr=[],[]
for i in range(n):
    arr.append(list(map(int,input().split())))
    
arr.sort(key= lambda x: (x[1], -x[0])) #날짜 오름차순, 돈 내림차순

for p, d in arr:
    heapq.heappush(que, p) #무작정 돈을 넣고, que길이를 봤을 때, d가 1일 때는 하나만 들어가야하고, 2일 때는 두 개가 들어가야 함
    if(len(que)>d):
        heapq.heappop(que)

print(sum(que))
''' last조건문이 틀렸는데 
d = 1 1 4 4
p = 5 5 5 5 의 경우,
d = 1 4 4가 최대가 되는데, d != last일 때로 하면 틀림
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
'''