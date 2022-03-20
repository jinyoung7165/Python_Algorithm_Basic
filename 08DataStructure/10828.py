#백준 10828 - 스택
from sys import stdin
input = stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    c = command[0]
    if c == 'push': 
        stack.append(int(command[1]))
    else:
        l = len(stack)
        if c == 'pop':
            if l == 0: 
                print(-1)
            else: 
                print(stack.pop())
        elif c == 'size':
            print(l)
        elif c == 'empty':
            if l == 0: print(1)
            else: print(0)
        else:
            if l == 0: print(-1)
            else: print(stack[-1])