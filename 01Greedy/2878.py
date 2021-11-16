#백준 2878 - 캔디캔디
#사탕 m개 -> n명에게 분배. 각 사람의 요구에 비해 못 받는 개수의 제곱의 합을 최소로
#요구의 합-m =부족한 양 -> 각 사람에게 분배해서 제곱의 합 최소화
#최대한 부족한 양을 골고루 분배
from sys import stdin
input=stdin.readline
m,n=map(int,input().split())  #사탕 수, 사람 수
demand=[] #사람 별 요구
min=0 #제곱의 합 최소
for i in range(n):
    demand.append(int(input()))
lack=sum(demand)-m #총 부족한 양
demand.sort(reverse=True) #요구량 많은 사람 순

if(lack<=n): #부족<=N명 => 제곱 합 최소=각 사람마다 부족 1씩 더함=부족 개수
    min=lack
else: #요구량 가장 많은 사람 것부터 빼는 게 중요. 부족한 양 고르게 분포해야 함
    temp=[]
    for i in demand:
        if i==1:  #요구량이 1이면 안 주면 됨
            min+=1
            temp.append(demand.index(i)) #요구량이 1인 인덱스 저장
            lack-=1
            n-=1 #사람 수
    for i in temp:
        del demand[i]
    for i in demand:
        share=lack//n #몫
        remain=lack%n #나머지
        if(remain<1): #나눠 떨어지면
            min+=n*(share**2) #모든 멤버들에게 똑같이 부족 배분
            break
        if(remain==1):
            min+=((share+1)**2) #몫+나머지1
            lack-=share+1
            n-=1 #사람 수
        if(remain>1):
            min+=((share+1)**2) #일단 1만 주고 다른 친구들에게 나눠주거나, 자기가 모든 나머지 가져야할 수도 있음
            lack-=share+1
            n-=1 #사람 수
print(min%(2**64))

                    
            
    
    
