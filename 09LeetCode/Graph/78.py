#부분 집합
#[1,2,3] => [[],[1],[2],[3],[1,2],[1,3],[1,2,3],[2,3]]
def subset(nums = [1,2,3]):
    result = []
    
    def dfs(idx, path):
        result.append(path) #바로 추가
        
        for i in range(idx, len(nums)): #어차피 idx가 len(nums)보다 크면 range 실행안됨
            dfs(i+1, path + [nums[i]]) #다음 원소의 인덱스와 현재까지의 경로 전달
            
    dfs(0, [])
    
    return result
print(subset())