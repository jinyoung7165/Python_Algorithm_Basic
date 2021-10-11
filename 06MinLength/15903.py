#백준15903 - 카드 합체 놀이
#자연수 쓰인 카드 n장. 
#합체 m번 후, n장의 카드를 모두 더한 점수를 가장 작게
#1.x번 y번 카드 골라 두 장 합
#2.합을 x,y카드에 모두 덮어 씀
from sys import stdin
import heapq
input=stdin.readline
n,m=map(int,input().split()) #카드 수,합체 수
card=list(map(int,input().split())) #맨 처음 카드 상태
que=[] #작은 것 먼저 나오게 할 것
for i in range(n):
    heapq.heappush(que,card[i])

for i in range(m):#수행
    temp=heapq.heappop(que)+heapq.heappop(que) #가장 최소 두 개
    heapq.heappush(que,temp)
    heapq.heappush(que,temp) #카드 두 개 모두 넣음

print(sum(que))