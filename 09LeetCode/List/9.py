#Container with Most Water
#가장 많은 물을 수용할 수 있는 두 개의 축 찾은 후, 물의 양 출력
#너비, 높이 모두 고려
#height = [1,8,6,2,5,4,8,3,7] 각 기둥 사이에 공간 존재
#Output: 49
#Input: height = [1,1]
#Output: 1
class Solution:
    def maxArea(self, height) -> int:
        #가장 많은 물을 저장할 수 있는 두 개의 축 구하라
        #양 옆 높이 max중 작은 높이에 맞춰 width*높이
        left, right = 0, len(height) - 1 #x
        left_max, right_max = height[left], height[right] #y
        capacity = 0
        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max <= right_max:
                capacity = max(capacity, left_max*(right-left))
                left += 1
            else:
                capacity = max(capacity, right_max*(right-left))
                right -= 1
                
        return capacity