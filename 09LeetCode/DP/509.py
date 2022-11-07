#Fibonacci
'''
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
'''
#가장 효율적. 두 변수만 이용해 공간 절약 O(n) -> O(1)
def fib(n):
    x, y = 0, 1
    for i in range(0, n):
        x, y = y, x+y
    return x

#타뷸레이션. 상향식 풀이
def fib(n):
    dp = [0] * (n+1)
    if n > 0: dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

#메모이제이션. 하향식 풀이 ->재귀. 이미 계산한 값 바로 리턴
#n=5일 때 fib(2), fib(3) 한 번만 계산
#n커질수록 효율적
import collections

class Solution:
    dp = collections.defaultdict(int)
    def fib(self, n):
        if n <= 1: return n
        if self.dp[n]: #값 존재하면 바로 리턴
            return self.dp[n]
        
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]