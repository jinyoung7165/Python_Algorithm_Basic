#Top k Frequent Elements
#상위 K번 이상 등장하는 요소를 추출
#nums=[1,1,1,2,2,3], k=2  => [1,2]
import collections
import heapq
def topKFrequent(nums=[1,1,1,2,2,3], k=2):
    result = []
    freqs = collections.Counter(nums)
    freqs_heap = []
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f)) #최대빈도 우선순위
    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    return topk
    #result =list(zip(*collections.Counter(nums).most_common(k)))[0] #Counter(nums).most_common(k):[(1, 3), (2, 2)], *: unpacking시 안에 들어있는 시퀀스의 인덱스순서를 묶어 언패킹 (1,2) (3,2)
    #return result
    
print(topKFrequent())