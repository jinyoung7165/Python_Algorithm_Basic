#Olog(n)
#이진탐색트리:정렬된 구조를 저장하고 탐색하는 '자료구조'
#이진 검색:정렬된 배열에서 값을 찾아내는 '알고리즘'
#배열 크기가 크고, 찾아야하는 값이 항상 앞에 있는게 아니라면 bisect 활용
def search(self, nums, target) -> int:
    def binary_search(left, right):
        if left <= right:
            mid = (left+right) // 2

            if nums[mid] < target:
                    return binary_search(mid+1, right)
            elif nums[mid] > target:
                return binary_search(left, mid-1)
            else: return mid
        else : return -1
    return binary_search(0, len(nums)-1)