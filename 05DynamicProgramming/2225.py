#합분해
#0부터 N까지 정수 K개를 더해 합이 N이 되는 경우의 수? 순서가 바뀌면 다른 것. 한 개의 수 여러 번 쓸 수 있음. 답을 10**9로 나눈 나머지?
#n, k에 대한 관계를 표로 나타내보면
#dp[i][j] = dp[i-1][j] + dp[i][j-1] (i,j>2)
n, k = map(int, input().split())
dp = [[1]*(n+1) for _ in range(k+1)]
    
for i in range(2, k+1):
    dp[i][1] += dp[i-1][1]
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(str(dp[k][n] % 1000000000))
