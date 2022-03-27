#세 수의 합
#배열을 입력 받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력
#입력: [-1,0,1,2,-1,-4]
#출력: [ [-1,0,1], [-1,-1,2] ]
def threesum(nums = [-1,0,1,2,-1,-4]):
    nums.sort()
    results = []
    #원래라면 i,j,k 브루트포스 삼중반복문
    #i:현재 값 ->방향. left=i+1, right=len(nums)-1번째 수
    #i+j+k 더해서 0 만들자
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: #이미 본 조합만 나올 것
            continue
        left, right = i+1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > 0: right -= 1
            elif sum < 0 : left += 1
            else:
                results.append([nums[i],nums[left],nums[right]])
                while left < right and nums[left] == nums[left+1]: #어차피 본 조합만 나옴
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1   
                left += 1
                right -= 1 #sum이 0인 상황이므로 left, right 둘다 움직여
            
    return results
print(threesum())