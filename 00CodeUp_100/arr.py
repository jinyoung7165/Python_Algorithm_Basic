a=input()
a=int(a)
b=input().split()
#b=b.reverse()   #안됨
b.reverse() #그 자체로 바뀐다

for i in range(0,a):
    print(b[i],end='')
