#빗물 트래핑
#땅의 높이를 받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산
#입력: [0,1,0,2,1,0,1,3,2,1,2,1]
#출력: 6
#-> 탐색하며 자신보다 크거나 같으면 자신만큼 쌓임 * 이동 칸 수
#자신보다 작으면 큰 거 나올 때까지 * 이동 칸 수  - (중간에 만난 작은 높이들)
#left, right 비교할 일 있으면 투 포인터로 풀자!
#투포인터 축소하면서 leftmax-> max <-rightmax. (더 낮은 쪽 max-현재 높이)만큼 쌓임
def raintrap(input = [0,1,0,2,1,0,1,3,2,1,2,1]):
    left, right = 0, len(input) - 1
    left_max, right_max = input[left], input[right]
    volume = 0 #쌓인 양
    while left < right: #투포인터(left, right) 축소하며 이동
        left_max, right_max = max(left_max, input[left]), max(right_max, input[right])
        if left_max <= right_max:
            volume += left_max - input[left] #max 중 더 낮은 쪽-현재높이만큼 쌓임
            left += 1 #왼쪽 포인터(현재위치) 이동
        else:
            volume += right_max - input[right]
            right -= 1
    return volume
        
print(raintrap())