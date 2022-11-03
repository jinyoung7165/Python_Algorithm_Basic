#Queue Reconstruction by Height
import heapq
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        que, result = [], []
        for h, k in people:
            heapq.heappush(que, (-h, k))
        while que:
            person = heapq.heappop(que)
            result.insert(person[1], [-person[0], person[1]])
        return result