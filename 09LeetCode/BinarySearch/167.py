#Two sum <- input arr is sorted
from bisect import bisect
import numbers
#투포인터 O(n)
def twoSum(self, nums, target):
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return left + 1, right + 1 #인덱스가 1부터 시작 조건

#bs O(nlogn) -> 성능 개선해서 투포인터랑 시간 같아짐
def twoSum(self, nums, target):
    for k, v in enumerate(nums):
        expected = target - v #만들어야 하는 남은 수
        i = bisect.bisect_left(numbers, expected, k+1) #왼쪽범위(k+1)인덱스부터 지정->속도 개선
        if i < len(nums) and nums[i] == expected: #expected찾았다
            return k+1, i+1