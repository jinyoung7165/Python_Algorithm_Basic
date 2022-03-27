#two sum 두 수의 합
#덧셈해 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
#입력: nums = [2,7,11,5], target = 9
#출력: [0,1]
#인덱스를 찾는 문제기 때문에 bisect로 풀면 정렬 때문에 인덱스 사라짐!!
'''
def twosum(nums = [2,7,11,5], target = 9):
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i+1:]: #전체에서 자신을 뺀 나머지를 비교
            return [nums.index(n), nums[i+1:].index(complement) + (i+1)]
            #nums[i+1:].index(complement)가 0이라면 원래 배열에서의 인덱스는 i+1
'''
def twosum(nums = [2,7,11,5], target = 9): #딕셔너리로 빠르게 인덱스 조회
    nums_map = {}
    for i, n in enumerate(nums):
        nums_map[n] = i #숫자에 대한 값을 인덱스로 지정
    
    for i, n in enumerate(nums): #i != nums_map[target - n]로 같은 수 두 번 나오는 것 방지
        if target - n in nums_map and i != nums_map[target - n]:
            return [i, nums_map[target - n]]
        
        
    
print(twosum())