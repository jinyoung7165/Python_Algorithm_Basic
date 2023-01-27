#Convert Sorted Array to Binary Search Tree
#오름차순으로 정렬된 배열을 높이 균형 이진 탐색 트리로 변환
#높이 균형:두 subTree간 높이 차가 1이하
#[-10,-3,0,5,9] -> [0,-3,9,10,null,5]
def sortedArrToBST(self, nums):
    if not nums:
        return None
    
    mid = len(nums) // 2 #중앙값
    node = TreeNode(nums[mid])
    node.left = self.sortedArrToBST(nums[:mid])
    node.right = self.sortedArrToBST(nums[mid+1:])
    
    return node