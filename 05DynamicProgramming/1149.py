#백준 1149 - RGB거리
from sys import stdin
input=stdin.readline
n=int(input())
cost=[]  #dp[j]=dp[i]+dp[j-i]   dp[j]+=아무갑
for _ in range(n): #각 집마다
    cost.append(list(map(int,input().split()))) # 각 색마다 비용 [[100,200,300],[100,2,3]]
#dp[i]: i번째 집까지 고려했을 때 최소 비용. i번째 집을 각 색마다 칠했을 때의 경우를 따로 저장

for i in range(1,n): #모든 집 색칠
        cost[i][0]+=min(cost[i-1][1],cost[i-1][2]) #현재 집에 R
        cost[i][1]+=min(cost[i-1][0],cost[i-1][2]) #현재 집에 G
        cost[i][2]+=min(cost[i-1][0],cost[i-1][1]) #현재 집에 B
        
print(min(cost[n-1][0],cost[n-1][1],cost[n-1][2]))