#포도주를 선택하면 모두 마셔야함.원래 위치에 둬야함
#연속으로 놓여있는 3잔을 모두 마실 수는 없음
#1-n번호의 포도주 잔이 순서대로 놓여있음
#각 잔의 포도주의 양 주어짐. 
#최대한 먹을 수 있는 양?
#dp[i]:i번째까지의 최대 포도주 양
#dp[0]:wine[0] / 0
#dp[1]:wine[0]+wine[1] / 0
#dp[2]:max(dp[1], wine[0]+wine[2], wine[1]+wine[2]) //연속 3개 못마시므로
#dp[3]:max(wine[1]+wine[2] = dp[2], wine[0]+wine[1]+wine[3] = dp[1] + wine[3], wine[0]+wine[2]+wine[3])
#dp[i]:max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])
#max(나 뺌, 이전 거 뺌, 전전 거 뺌)
n = int(input())
dp = [0] * n
wine = [int(input()) for _ in range(n)] #각 와인의 양

dp[0] = wine[0] #무조건 하나의 잔은 존재

if n > 1: #잔이 두 개 이상이면
    dp[1] = wine[0]+wine[1]
if n > 2:
    dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])
for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
    

print(dp[n-1])