#Maximum Star Sum of a Graph
#A star graph is a subgraph of the given graph having a center node containing 0 or more neighbors. 
# = subset of edges of the given graph such that there exists a common node for all edges.
class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        
        m = defaultdict(list)                                                                 
        
        for x,y in edges:       
            
            if vals[y]>0:                    
                
                heapq.heappush(m[x], vals[y])   
                if len(m[x])>k:                 
                    heapq.heappop(m[x])         
            
            if vals[x]>0:
                heapq.heappush(m[y], vals[x])  
                if len(m[y])>k:
                    heapq.heappop(m[y])
            
            
        res = -math.inf
        for i in range(len(vals)):           
            tot = vals[i]                      
            for nei_value in m[i]:              
                tot+=nei_value                
                
            res = max(res, tot)                        
        return res     