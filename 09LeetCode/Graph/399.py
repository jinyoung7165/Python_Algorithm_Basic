#Evaluate Division
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        group={}
        g=defaultdict(list)
        d = {}
        vals={}
        
        for eq,v in zip(equations,values):
            x,y=eq
            g[x].append(y)
            g[y].append(x)
            d[(x,y)]=v
            d[(y,x)]=1/v
        def dfs(var,val,root):
            if var not in vals:
                vals[var]=val
                group[var]=root
                for nei in g[var]:
                    dfs(nei,val*d[(nei,var)],root)
        for key in g:
            dfs(key,1,key)
        res=[]
        for x,y in queries:
            if x not in vals or y not in vals or group[x]!=group[y]:
                res.append(-1.0)
                continue
            res.append(vals[x]/vals[y])
        return res