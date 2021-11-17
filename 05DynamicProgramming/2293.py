#백준 2293- 동전1
#n종류의 동전-> 총 합 k원
#경우의 수?
#dp[i]:총 i원을 만들 수 있는 동전 가짓수
from sys import stdin
input=stdin.readline
n,k=map(int,input().split())
val=[]
dp=[0 for _ in range(k+1)] #0~k
for _ in range(n):
    i=int(input())
    val.append(i)

dp[0]=1 #dp[j]=dp[j]+dp[0]처럼 동전 하나 써서 본인이 되는 경우는 1
for i in val: #동전 별 k까지의 각 금액을 만들기 위한 경우가 존재하면 기록 갱신 -> 모든 동전의 경우 합
    for j in range(i,k+1): #i~k번째까지의 j를 만드는 경우는 dp[j-i]. j-i원의 금액을 만드는 경우(나머지 i원은 동전의 단위이므로 동전 하나 더하면 됨)
        dp[j]+=dp[j-i]
        
print(dp[k])        