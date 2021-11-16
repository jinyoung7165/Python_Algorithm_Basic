#백준 1946- 신입사원
#A의 성적이 어떤 B의 성적에 비해 두 순위가 모두 떨어지면 탈락
#최대 선발 수?
from sys import stdin
input=stdin.readline
t=int(input()) #테스트 케이스

for _ in range(t):
    n=int(input()) #지원자 수
    score=[] #서류,면접
    for _ in range(n):
        score.append(list(map(int,input().split())))
    max=n
    score.sort()
    m=score[0][1] #서류 1등의 면접 순위
    for i in range(1,n): #2등부터 마지막까지
        if(score[i][1]>m):#본인보다 서류 순위 낮은 사람보다 면접도 순위 클 때 탈락
            max-=1
            continue
        m=score[i][1] #면접 더 낮은 순위로 갱신
    print(max)
