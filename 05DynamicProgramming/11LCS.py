#백준 9251 - 최장 공통 부분 수열
#acaykp * capcak => acak
#dp[i][j]: S1의 i,S2의 j번째까지 비교해서 공통 수열개수
#행,열 다른 문자 나올 때 [i-1][j] vs [i][j-1] 비교해서 더 큰 값
#행,열 같은 문자 나올 때 이전 값+1
from sys import stdin
input=stdin.readline
a=input().strip().upper()
b=input().strip().upper()
dp=[[0] *(len(a)+1) for _ in range (len(b)+1)]
#len(a)열 len(b)행 배열 
for i in range(len(b)):
    for j in range(len(a)):
        if b[i]==a[j]: #[0][0]의 이전 대각선은 없기 때문에 1행 1열부터 dp삽입
            dp[i+1][j+1]=dp[i][j]+1
        else:
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
print(dp[-1][-1])
