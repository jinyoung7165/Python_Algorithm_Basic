#x가 3으로 나눠떨어지면, 3으로 나눔
#2로 나눠떨어지면, 2로 나눔
#1을 뺌
#정수 N이 주어졌을 때, 세 연산을 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력

n = int(input())
dp = [0 for _ in range(n+1)] #n - 1*(n-1)번 빼면 1이 된다

#dp[i]: i에서 1이 되기까지의 연산 횟수
#dp[0], dp[1]: 0번
#dp[2]: 1번. min(dp[1]+1, dp[2]//2이면 + dp[1] 1)
#dp[3]: 1번. min(dp[2]+1, dp[3]//3이면 + dp[1] 1)
#dp[4]: min(dp[3]+1, dp[4]//2 이면 + dp[2])
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
        dp[i] = dp[i//2] + 1
    if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
        dp[i] = dp[i//3] + 1

print(dp[n])