#백준 10844- 쉬운 계단 수
#길이가 n인 계단 수 총 몇 개 있는지. 0으로는 시작 못함
#1자리->9개, 2자리->17개
#최대 n :100, dp[i][j]: i자리 수가 j로 끝날 때 가능한 계단 수
n = int(input())
dp = [[0 for i in range(10)] for j in range(101)] #(0-100)자리 (0-9)로 끝나는 수
for i in range(1, 10): #1의 자리 수 0-9
    dp[1][i] = 1
for i in range(2, n + 1): #2의 자리 수부터 n자리 수까지
    for j in range(10): #0-9로 끝나는 수
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % 1000000000)