#Number of provinces
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        processed = set()
        cnt = 0
        for r in range(len(M)): 
            if r not in processed:
                cnt += 1
                stack = [i for i,v in enumerate(M[r]) if i != r and v == 1]
                while stack:
                    curr = stack.pop()
                    if curr in processed: continue
                    processed.add(curr)
                    stack.extend([i for i,v in enumerate(M[curr]) if i != r and v == 1])
        return cnt