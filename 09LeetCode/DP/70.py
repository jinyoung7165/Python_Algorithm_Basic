#Climbing Stairs
import collections

class Solution:
    dp = collections.defaultdict(int)
    
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n-1) + self.climdbStairs(n-2)
        return self.dp[n]