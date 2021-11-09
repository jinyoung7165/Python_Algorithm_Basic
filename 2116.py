#백준 2116- 주사위 쌓기
#위아래 주사위의 맞댄 면의 숫자가 같아야함
#모두 쌓았을 때, 주사위별 4 옆면의 숫자합이 최대
#첫 번째 주사위는 막 놓을 수 있음
from sys import stdin
input=stdin.readline
n=int(input()) #주사위 수
dice=[]
rotate={0:5,1:3,2:4,3:1,4:2,5:0} #반대편 면
for i in range(n):
    dice.append(list(map(int,input().split())))

maxsum=0
for i in range(6): #첫 번째 주사위의 i번째 면을 위로 둘 때
    temp=[1,2,3,4,5,6] #옆면이 될 수 있는 값
    upper=dice[0][i]
    temp.remove(dice[0][i]) #윗면의 수 제거
    temp.remove(dice[0][rotate[i]]) #아랫면의 수 제거
    sum=max(temp)
    for j in range(1,n): #두 번째부터 마지막
        temp=[1,2,3,4,5,6]
        temp.remove(upper) #아랫면의 수 제거
        up_idx=rotate[dice[j].index(upper)] #윗면의 인덱스
        upper=dice[j][up_idx] #윗면의 수
        temp.remove(upper) #윗면의 수 제거
        sum+=max(temp)
        if(j==n-1 and sum>maxsum): maxsum=sum
print(maxsum)

