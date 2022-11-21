#Next Permutation
#return 없이 배열 안 변경해라
'''
Input: nums = [1,2,3]
->[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]
Output: [1,3,2]

Input: nums = [3,2,1]
Output: [1,2,3]

Input: nums = [1,1,5]
Output: [1,5,1]
'''
#[1,2,3]을 받으면 그 다음 큰 숫자인 [1,3,2]을 반환하면 됩니다.
#123<132로 생각 -> 일의 자리 숫자(맨 오른쪽)부터 올라가면서 숫자 더 키울 생각
#132,213(next)
#뒤의 수보다 앞의 수 커지면 전체 수 커짐(다음 수)
class Solution:
    def nextPermutation(self, nums) -> None:
        i = j = len(nums)-1 #일의 자리
        #뒤의 것보다 앞에 것 큰 순간 잡아라
        #작아지다 커지는 시점 -> i 이후로는 바른 정렬. 대신 i 뒤에 바른 곳 찾아 끼워넣기 필요
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1  #i==0이면 숫자가 내림차순으로 정렬된 것 -> 오름차순으로 정렬해주면 됨
        if i == 0: #321
            nums.reverse() #123
            return
        
        k = i - 1
        while nums[j] <= nums[k]: #앞의 수가 뒤의 수보다 큼-> 뒷자리 수 swap하면 커짐
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k+1, len(nums)-1
        while l < r: #오름차순 -> 내림차순
            nums[l], nums[r] = nums[r], nums[l]
            l += 1 ; r -= 1