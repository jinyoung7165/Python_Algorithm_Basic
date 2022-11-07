#Maximum Subarray
#최대 서브 배열
#nums배열 주어지면 가장 큰 sum을 가진 (순서 동일.연속된)서브 배열의 sum
#nums = [-2,1,-3,4,-1,2,1,-5,4] -> [4,-1,2,1] => 6
#nums = [1] -> [1] => 1
#nums = [5,4,-1,7,8] -> [5,4,-1,7,8] => 23
#O(n) 쓰고 싶으면 분할정복 사용하라
def maxSubArray(nums):
    length = len(nums)
    if length == 1: return nums[0]
    for i in range(1, length):
        nums[i] = max(nums[i-1] + nums[i], nums[i])
        
    return max(nums)