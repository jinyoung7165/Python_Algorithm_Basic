def solution(n,stages):#실패율 내림차순으로 스테이지번호 담긴 배열 리턴
    stages.sort(reverse=True) #값: 1-n+1
    clear=[0]*(n+2) #0-n+1. 현재stage클리어수는 다음stage clear+unclear수
    result=[0]*(n+2) #실패율 저장. 먼저 unclear수부터 저장
    for i in stages: #i스테이지에 멈춰있음(unclear)
        result[i]+=1 #해당 스테이지에 멈춰있는 사람 수
        if(i!=1):clear[i-1]+=1 #이전 스테이지 클리어 수+1(현재 스테이지 unclear수)
    for i in range(n+1,0,-1): #n+1~1스테이지
        clear[i-1]+=clear[i] #전 단계를 clear한 사람들은 다음단계를 clear한 사람들과 포함
        if(clear[i]==0):result[i]=1 #실패율은 1
        elif result[i]+clear[i]==0:result[i]=-1 #아무도 오지 않았을 때
        else:result[i]=result[i]/(result[i]+clear[i]) #현재 단계 실패율
    print(result)
    result=result[1:n+1] #1-n단계의 실패율
    arr=[]*n
    print(result)
    for i in range(n):
        arr.append((result[i],i))
    arr.sort(key=lambda x:(-x[0])) #내림차순으로 정렬
    print([i[1]+1 for i in arr])
    return [i[1]+1 for i in arr]
solution(2,[1,1])
