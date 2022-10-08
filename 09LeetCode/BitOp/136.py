#배열의 원소들 중 한 번만 주어진 원소 존재, 나머지는 두 개씩
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result