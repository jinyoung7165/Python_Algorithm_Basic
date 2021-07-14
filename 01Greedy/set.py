#11723 - 집합
'''
공집합 S
add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다. 
'''
import sys

s={''} #공집합
m=int(input()) #연산의 수
for _ in range(m):
    op=sys.stdin.readline().split()
    if len(op)==1:#all또는 empty
        if op[0]=='all':
            s={i for i in range(1,21)}
        else: s.clear()
        continue
    command,target=op[0],op[1] 
    target=int(target)  
    if command=='add':
        s.add(target)
    elif command=='check':
        print(1 if target in s else 0)
    elif command=='remove':
        s.discard(target)
    else:
        if target in s:s.discard(target)
        else:s.add(target)
#check연산이 주어질 때마다 결과 출력