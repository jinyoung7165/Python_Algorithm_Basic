#백준 18115 - 카드 놓기
#손에 있는 카드를 하나씩 바닥에 쌓으려한다. 사용할 수 있는 기술 3개
#1. 제일 위 카드 1장을 내려놓는다
#2. 위에서 두 번째 카드를 내려놓는다. 카드가 2장 이상일 때만
#3. 제일 밑 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만
#처음에 N장 들고 있음(1-N 중복x).모두 내려놓았을 때, 위에서부터 순서대로 1,2,..n
#처음 카드의 상태를 출력해라
from sys import stdin
from collections import deque
input=stdin.readline
n=int(input())

que=deque([i for i in range(n,0,-1)])#5,4,3,2,1
skills=list((input().split())) #각 카드별 쓴 기술
origin=deque()
#결과큐->origin큐. 결과 큐의 마지막부터 수행 순서 거꾸로
for count in range(n): #popleft먼저 들어간 5부터 꺼낸다
    skill=skills[n-count-1] #해당 카드에 사용한 기술
    if(skill=='1'):#결과의 가장 아래 카드를 origin의 맨 위에
        origin.appendleft(que.pop())
    elif(skill=='2'):  #origin의 밑에서 두 번째.count: 0,3->1,2
        origin.insert(1,que.pop())
    else:#카드를 origin의 가장 아래에
        origin.append(que.pop())
'''
for i in origin:
    print(i ,end=" ")
'''
print(*origin)
