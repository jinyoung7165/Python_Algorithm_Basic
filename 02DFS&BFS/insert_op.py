#N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것
import sys
n=int(input()) #숫자의 개수
a=[]
a.extend(list(map(int,input().split())))
p,m,mul,div=map(int,input().split())
minn=sys.maxsize
maxn=-sys.maxsize-1
def cal(num,index,plus,minus,mul,div): #계산결과,몇 번째 숫자와의 계산이었는지, 사용할 수 있는 연산자 개수 몇 개 남았는지
    global minn,maxn
    if index==n:#방금 연산에 사용한 것이 마지막 원소였을 때
        maxn=max(num,maxn) #최댓값 구함
        minn=min(num,minn) #최솟값 구함
        return #종료
    else:
        if plus: #아직 plus연산자가 남아있을 때
            cal(num+a[index],index+1,plus-1,minus,mul,div)
        if minus: #아직 minus연산자가 남아있을 때
            cal(num-a[index],index+1,plus,minus-1,mul,div)
        if mul: #아직 mul연산자가 남아있을 때
            cal(num*a[index],index+1,plus,minus,mul-1,div)
        if div: #아직 div연산자가 남아있을 때
            cal(int(num/a[index]),index+1,plus,minus,mul,div-1)
       
cal(a[0],1,p,m,mul,div) #첫번째 숫자와 두번째 숫자(인덱스1)의 연산
print(maxn)
print(minn)