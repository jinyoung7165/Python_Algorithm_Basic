#백준 7785 - 회사에 있는 사람
#로그가 주어졌을 때, 현재 회사에 있는 사람 몇 명인지
#로그가 기록된 수 n. 사람 enter/leave 주어짐
#대소문자가 다른 경우 다른 이름
#출력: 사전 역순
from sys import stdin
input=stdin.readline
n=int(input())
log=dict()
result=[]
for i in range(n):
    name,el=list(input().split())
    log[name]=el
for i in log:
    if log[i]=="enter":
        result.append(i)
result.sort(reverse=True)
for i in result:
    print(i)