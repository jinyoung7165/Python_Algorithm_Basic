#백준 3649 - 로봇 프로젝트
#x길이의 구멍을 두 조각의 블락으로 막는다
#각 테스트 케이스마다 한 줄에 하나씩 x길이를 만들 수 있는 두 조각이 없으면 danger출력
#존재하면 yes |l1-l2| 중 가장 큰 거 출력
from sys import stdin
input = stdin.readline

while True:
    try:
        x = int(input()) #구멍의 너비(c미터 단위)
        n = int(input()) #존재하는 블락의 개수 
        length = [] #각 블록의 길이(n미터 단위)
        #최대 10^(-8) = 1e8
        for i in range(n):
            length.append(int(input()))

        x *= int(1e7)
        length.sort()
        left, right = 0, n - 1
        temp, result = -1, []
        while (left < right):
            sum = length[left] + length[right]
            if sum == x and  temp < abs(sum):
                temp = abs(sum)
                result.append([length[left], length[right]])
            elif sum < x:
                left += 1
            else:
                right -= 1
        if temp != -1:
            print("yes", *result[0])
        else:
            print("danger")
    except:
        break
