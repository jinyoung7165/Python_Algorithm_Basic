#Sort Colors
#빨강0 흰1 파랑2 -> 순서대로 인접하는 "InOrder제자리 정렬" 주어진 배열만 사용하는 것
#red, white가 모두 0에서 시작. blue는 배열의 길이가 됨
#1을 기준으로 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 스왑
#red, blue가 중앙 쪽으로 이동하며 가까워짐(투포인터 느낌)
#red는 1(중앙)보다 작은 index+1 지점
#blue는 1(중앙)보다 큰 index+1지점
#white와 blue겹쳐지며 비교 완료
#퀵 정렬(2부분 분할) -> 3부분 분할로 개선
from ast import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)
        
        while white < blue:
            if nums[white] < 1: #red
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1: #blue
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else: #white
                white += 1
                
                
    def sortColors(self, nums: List[int]) -> None:
        redCount= nums.count(0)
        whiteCount= nums.count(1)
        blueCount= nums.count(2)
        #각 개수 세서 red, white, blue순으로 채워나감
        for x in range(len(nums)):
            if redCount>0:
                nums[x]=0
                redCount-=1
            elif whiteCount>0:
                nums[x]=1
                whiteCount-=1
            elif blueCount>0:
                nums[x]=2
                blueCount-=1