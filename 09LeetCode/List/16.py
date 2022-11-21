#3Sum Closest
#target값과 가장 가까운 3sum을 구하라(답 무조건 하나)
from ast import List

def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums) - 1
        distance = float('inf') #sys.maxsize 진짜 느림
        
        for i in range(length - 1):
            j, k = i+1, length
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                temp = nums[i] + nums[j] + nums[k] - target
                if abs(temp) < abs(distance):
                    distance = temp
                if temp > 0:
                    k -= 1
                elif temp < 0:
                    j += 1
                else: return target
            
        return distance + target


