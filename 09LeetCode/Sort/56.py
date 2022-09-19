#겹치는 구간을 병합하라
#[[1,3],[2,6],[8,10],[15,18]]
#=> [[1,6],[8,10],[15,18]] 2가 1,6사이에 들어감
from ast import List


def merge(self, intervals: List[List[int]])->List[List[int]]:
    merged = []
    for i in sorted(intervals, key = lambda x: x[0]): #첫번째 원소 기준으로 정렬
        if merged and i[0] <= merged[-1][1]: #다음 리스트의 첫번째 원소가 이전 리스트의 두번째 원소보다 작으면 겹침
            merged[-1][1] = max(merged[-1][1], i[1]) #이전 원소의 두번째 원소 갱신
        else:
            merged += [i] #i를 더하면 i의 원소를 append해버림
    return merged
    