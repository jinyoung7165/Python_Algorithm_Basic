#한 방향 원형으로 순회하면서 해당 원소보다 처음으로 큰 수 기록
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [] #자기보다 더 큰 원소를 기다리는 인덱스
        size = len(nums)
        result = [-1] * size
        
        for i in range(size*2): #자신 이후 - 자신까지 원형으로 돌 것
            while stack and nums[stack[-1]] < nums[i%size]: #현재 원소가 stack에서 기다리는 원소보다 클 때
                result[stack.pop()] = nums[i%size] #답 기록
            stack.append(i%size)
        return result