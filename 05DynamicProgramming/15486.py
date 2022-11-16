#퇴사2
#오늘부터 N+1일째 되는 날 퇴사
#남은 N일 동안 최대한 많은 상담 -> 최대 수익?
#상담 걸리는 날 T, 수익 P
#하루에 여러 번 상담 불가
#1일부터 N일까지 순서대로 주어진다
from sys import stdin

input = stdin.readline
n = int(input())

t, p = [], []
dp = [0 for _ in range(n+1)] #n+1일까지의 최대 수익

for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

m = 0 #현재까지의 최대 수익
for i in range(n):
    m = max(m, dp[i]) #이미 누적돼 있을 경우 비교
    if i + t[i] > n: continue #n일 넘기면 누적x
    #현재 강의 선택 시 다음 강의에 영향을 줌 다음 강의가 이미 큰 경우 현재 선택x
    dp[i+t[i]] = max(m+p[i], dp[i+t[i]])

print(max(dp))