#n=7인 경우, 1~7일 동안만 상담 가능.
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
'''n=7
i   0 1 2 3 4 5 6 7
t 3 5 1 1 2 4 2
dp  해당 날짜의 상담을 할 시 벌 수 있는 돈
'''
'''dp(n-1)=max(a(n-1)+dp(n-1+T), dp(n))'''
#그날 일을 한 경우(끝난 다음 일까지 하게 된다)vs그날일을 안하고 다음날 일을 한 경우
