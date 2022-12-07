#조합의 합
#candidates = [2,3,6,7], target = 7
#candidates의 원소를 조합하여 합이 target이 되는 원소를 나열하라
# => [[7], [2,2,3]]
#모든 원소 탐색 중복조합. 백트래킹
#sum<0: 목표값 초과., sum=0:정답.결과리스트에 추가

result = []
candidates = [2,3,6,7]
target = 7

def dfs(sum, idx, path): #sum:만들어야 하는 남은 합
    if sum < 0: return
    if sum == 0:
        result.append(path)
        return
    
    for i in range(idx, len(candidates)):
        dfs(sum - candidates[i], i, path + [candidates[i]])
        
dfs(target, 0, [])
print(result)