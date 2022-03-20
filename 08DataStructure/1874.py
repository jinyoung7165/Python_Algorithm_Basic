#백준 1874 - 스택 수열
#1-n까지의 수를 스택에 넣고 뽑아 주어진 수열 생성
#어떤 순서로 push와 pop을 수행해야 하는지
#push는 +로, pop은 -로
from sys import stdin
input = stdin.readline
n =int(input())
sequence, stack, result = [i for i in range(1, n+1)], [], []

s = 1 #스택에 들어갈 오름차순 숫자
for i in range(n):
    num = int(input()) #입력한 수
    #top이 입력한 수보다 크면 안됨
    while (s <= num): #입력한 수가 될 때까지 오름차순으로 스택에 넣음
        stack.append(s)
        result.append('+')
        s += 1
    if stack[-1] == num :
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit()
for i in result:
    print(i)
