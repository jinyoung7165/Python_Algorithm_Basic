#Majority Element
#과반수를 차지하는 원소를 출력하라
import collections


def majorityElement(nums): #파이썬다운 방식. 가장 빠름
    return sorted(nums)[len(nums)//2]

def majorityElement(nums): #DP
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[num] == 0: #처음 기록할 때만 count -> 계속 count하는 것보다 훨씬 시간 줄임
            counts[num] = nums.count(num)
        
        if counts[num] > len(nums) // 2:#과반수 이상
            return num
        
def majorityElement(nums): #분할정복 mergesort처럼 쪼개다가 과반수 이상 후보에 해당하는 것만 위로 올림
    #재귀 특성상 DP보다 느림
    #7->3/4->1/2, 2/2로 나눠줌
    if not nums:
        return None
    if len(nums) == 1: #최소 단위 1이 될 때까지 쪼갬
        return nums[0]
    
    half = len(nums) // 2
    a = majorityElement(nums[:half])
    b = majorityElement(nums[half:])
    #현재 배열 nums를 a, b부분으로 쪼갬
    return [b, a] [nums.count(a) > half]  #a가 nums에서 과반수를 차지할 때 a, 그렇지 않으면 b리턴