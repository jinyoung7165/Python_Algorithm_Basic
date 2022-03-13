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
''' last조건문이 틀렸는데 왠지는 모르겠다. 반례가 없다
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

'''
import heapq
N=int(input())
lectures=[]

for i in range(N):
    lectures.append(list(map(int, input().split())))

# 리스트 둘째 인자를 오름차순으로 먼저 정렬 후 첫째 인자를 내림차순으로 정렬
# lectures.sort(key=lambda x: (x[1], -x[0])) 안해도됨
tmp=[] 

for q,d in lectures:
    heapq.heappush(tmp, q)
    print("push", tmp)
    if (len(tmp)>d):
        heapq.heappop(tmp)
        print("***pop***", tmp)

print(sum(tmp))
    
#===
'''