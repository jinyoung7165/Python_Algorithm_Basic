#각 child_i마다 만족하는 최소 쿠키gi를 가짐
#각 쿠키는 크기sj를 가지며 gi 이상이어야 아이가 받는다
#최대 몇 명의 아이들에게 쿠키를 줄 수 있는지
#g[1,2,3] s[1,1] -> 1명에게만 쿠키 줄 수 있음
#그리디

import bisect

def findContentChildren(g, s):
    g.sort()
    s.sort()
    
    child_i = cookie_j = 0
    #만족하지 못할 때까지 그리디 진행. s, g 둘 다 순회
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]: #만족
            child_i += 1 #인덱스 증가
        cookie_j += 1 #인덱스 증가
    return child_i

#bs(그리디와 성능 같음)
#하나의 리스트 순회하며 나머지는 이진검색으로 찾음
def findContentChildren(g, s):
    g.sort()
    s.sort()
    
    result = 0
    for i in s:
        #이진 검색으로 더 큰 인덱스 탐색
        index = bisect.bisect_right(g, i)
        if index > result:
            result += 1
    return result