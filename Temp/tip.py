#map 가로로 길게 입력 n번 받을 때
'''
n=3이고, 입력은 아래와 같이 들어올 때
0 1 0
1 0 1
0 0 1
'''
graph = [list(map(int, input().split())) for _ in range(n)]

#세로로 원소 하나씩 입력될 때
'''
1
2
3
'''
graph = [int(input()) for _ in range(n)]

#list안 특정 조건의 수 셀 때
count = [i for i in list if i == True]
print(len(count))

#각 원소 가로로 띄어서 프린트
#1 2 3 4 5
print(*count)