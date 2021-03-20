from collections import deque
#LIFO
que=deque()

que.append(5)
que.append(2)
que.append(3)
que.popleft()  #맨 앞쪽(왼쪽)에서 꺼냄
que.append(1)
que.append(4)
que.popleft()

print(que) #들어온 순서대로 출력(앞쪽부터 출력)
que.reverse() #역순으로 바꿈
print(que) #나중에 들어온 원소부터 출력
