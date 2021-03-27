#실패율:스테이지 도달했으나 클리어하지 못한 플레이어 /도달한 플레이어
#전체 스테이지 수 n,각 사용자가 현재 멈춰있는스테이지의 번호 배열stages
#실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열 return
#스테이지에는 1~n+1의 자연수. n+1은 마지막 스테이지까지 클리어한 사용자
#스테이지에 도달한 유저가 없는경우 해당 스테이지의  실패율은 0
#실패율이 높은 스테이지부터 내림차순으로 스테이지 번호
def solution(n,stages):
    reach=[0]*n
    unclear=[0]*n
    failure=[]
    answer=[]
    for i in range(n):#각 스테이지
        for j in range(len(stages)):#각 사용자
            if(i+1<=stages[j]):
                reach[i]+=1 #도달한 사람 수 추가
            if(i+1==stages[j]):
                unclear[i]+=1#도달했지만 클리어하지 못한 사람 추가
    for i in range(n):
        failure.append([unclear[i]/reach[i],i+1])
    failure.sort(key=lambda x:x[0],reverse=True)
    answer=[i[1] for i in failure]
    print(answer)
solution(5,[2,1,2,6,2,4,3,3])
solution(4, [4, 4, 4, 4, 4])

