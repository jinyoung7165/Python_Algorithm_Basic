#Largest Number
#항목(int)들을 조합해 만들 수 있는 가장 큰 수(str)
#[10,2] -> "210"
#insertionSort
from ast import List

class Solution:
    @staticmethod #this.method 호출 가능
    def to_swap(n1: int, n2: int) -> bool: #swap여부 bool판단. 이미 concat한 결과끼리 비교해야함
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]): #현재보다 sort된 이전 자리랑 비교
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1
             
        return str(int(''.join(map(str, nums)))) #00의 경우, int 0->다시 str
    

def largestNumber(nums): #[3,30,34,5,9]입력 시 9534303나옴, 답: 9534330. 303 vs 330 이미 concat한 결과끼리 자릿수마다 비교해야함
    nums = [str(n) for n in nums]
    nums.sort(reverse=True)
    
    return str(int(''.join(map(str, nums)))) #00의 경우, int 0->다시 str

print(largestNumber([0,0,99,199]))