import collections
from sys import maxsize

def maxSlidingWindow(self, nums, k):
    if not nums:
        return nums
    
    r = []
    for i in range(len(nums)-k+1):
        r.append(max(nums[i:i+k]))
    return r

#최적화 - max가 나오면 갱신
def maxSlidingWindow(self, nums, k):
    results = []
    window = collections.deque() #FIFO
    current_max = -maxsize
    for i, v in enumerate(nums):
        window.append(v)
        if i < k-1: #첫 번째 윈도우의 원소(K-1개 일단 채워놓음 -> K번부터 원소 하나씩 들어올 때마다 슬라이딩 윈도우 최댓값 비교)
            continue
        
        #새로 추가된 값이 기존 최댓값보다 큰 경우 교체
        if current_max == -maxsize: #이전에 있던 최댓값이 나가버림 -> 현재 윈도우의 최대 찾아야 함
            current_max = max(window)
        elif v > current_max: #새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            current_max = v
        results.append(current_max)
        
        #최댓값이 윈도우에서 빠지면 초기화 -> 최댓값 갱신해야 함
        if current_max == window.popleft(): #FIFO
            current_max = -maxsize
            
    return results

#최적화 - data많을 때 max너무 느림
def maxSlidingWindow(self, nums, k):
    results = []
    window = collections.deque() #FIFO
    
    for i, v in enumerate(nums):
        if window and i-window[0] == k: #윈도우 범위 초과
            window.popleft() #오래된 인덱스 꺼냄
        while window:
            if nums[window[-1]] < nums[i]:
                window.pop() #최신 원소가 현재 원소보다 작으면 꺼냄
            else: break
        window.append(i) #현재 원소 넣음(윈도우의 이전 원소보다 작음)
        
        if i >= k-1: #첫 번째 윈도우의 최대 원소부터 
            results.append(nums[window[0]])
        
    return results    