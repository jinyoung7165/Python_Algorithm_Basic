def solution(n,stages):
    failure={} #각 스테이지 번호를 키로 하는 딕셔너리
    reach=len(stages) #전체 사용자의 수(적어도 1레벨)
    for i in range(n):#각 스테이지
        if reach!=0:
            unclear=stages.count(i+1)#i+1번째(0부터 시작) 스테이지에 도달했지만 아직 클리어하지 못한 사용자
            failure[i]=unclear/reach #i번째 스테이지의 실패율
            reach-=unclear #다음 스테이지에 도달한 사람 수는 전체 사용자에서 이전 스테이지를 클리어하지 못한 사람 수를 뺌
        else:#이 스테이지를 도달한 사람이 아무도 없으면
            failure[i]=0
    return failure.sort(key=lambda x:failure[x],reverse=True)#딕셔너리의 value(실패율)을 기준으로 내림차순 정렬 후 키 값 반환
solution(5,[2,1,2,6,2,4,3,3])
solution(4, [4, 4, 4, 4, 4])

