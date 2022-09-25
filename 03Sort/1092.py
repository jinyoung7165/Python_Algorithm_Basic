#백준 1092 - 배
#각각 무게 제한있는 n개의 크레인에
#1분씩 n개의 크레인에 동시에 각 짐을 싣어 크레인이 배에 짐 전달
#모든 짐 다 싣기까지의 최소 시간 구하라. 다 못 싣는 경우 -1

from sys import stdin
from bisect import bisect_right

def main():
    input = stdin.readline
    n = int(input()) #크레인의 수
    crane = list(map(int, input().split()))
    crane.sort(reverse=True) #크레인의 무게 제한
    m = int(input()) #박스 수
    box = list(map(int, input().split()))
    box.sort()
    
    if crane[0] < box[-1]: #어차피 다 못 싣음
        return -1
    
    time = 0
    while box: #남은 box가 없을 때까지
        time += 1
        for c in crane:
            right = bisect_right(box, c) #범위가 큰 box배열에 crane을 끼워넣음
            if box and box[right-1] <= c: #box의 값이 crane이하면 box싣음
                box.pop(right-1) #해당 박스 제거
            else: break
    return time

print(main())