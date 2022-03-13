#백준2493- 탑
#일직선 위 N개의 탑->방향으로 설치
#각 탑에 왼쪽 방향으로 레이저 보내는 장치
#하나의 탑에서 보낸 신호는 하나의 탑에서만 수신 가능
#각각의 탑에서 발사한 레이저를 어느 탑에서 수신하는지
from sys import stdin
input=stdin.readline
n=int(input())
tower=list(map(int,input().split()))
result=[0 for _ in range(n)]
stack=[] #top의 인덱스를 저장
#직전에 들어온 값과 현재 탑 비교(앞에서부터)
#직전에 들어온 값이 크면 idx저장
#그렇지 않으면 더 이전의 값을 보기 위해 pop
#stack에 아무것도 없으면 현재 탑 넣음
for i in range(n):
    while stack: #비교할 앞의 탑들이 있으면
        if stack[-1][0]>=tower[i]: #앞의 탑이 더 크면
            result[i]=stack[-1][1]+1 #현재 탑에 대한 결과 도출
            break
        else: #앞의 탑에 신호 보낼 수 없으면
            stack.pop() #더 앞의 탑 본다
    stack.append((tower[i],i)) #현재 탑 넣는다

print(*result)



