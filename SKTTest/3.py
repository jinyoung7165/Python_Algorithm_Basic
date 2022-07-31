#1-m번 제공서비스, 1-n번 추가서비스
#요금제 1-3번에 따라 데이터, 서비스 다름
#각고객마다 이용하려는 데이터 이상을 제공하고, 이용하려는 서비스를 모두 포함하는 가장 작은 요금제의 번호 목록
#조건 만족하는 요금제가 없을 때 0담음
'''
요금제 정보
1번 데이터100  제공1,3     추가 1,3
2번 데이터500  제공1,3,4   추가 4
3번 데이터2000 제공1,3,4,5 추가 5
'''
'''
이용자 정보
데이터300  이용3,5 => 3번 요금제
데이터1500 이용1   => 3번
데이터100  이용1,3 => 1번
데이터50   이용1,2 => 0
=>[3,3,1,0]
'''
#n:서비스 수, 요금제 정보:plans, 이용정보:clients
#plans[i]="데이터 추가서비스" 문자열
#추가서비스도 공백으로 구분한 숫자 문자열(오름차순) 1-n 번호
#plans의 제공데이터는 중복x. 데이터 기준 오름차순
#clients[i]="데이터 서비스" 문자열(서비스 번호 오름차순) 1-n 번호
from collections import defaultdict
from bisect import bisect_left
def solution(n, plans, clients):
    dictplans = defaultdict(list)
    data = []
    idx = 0
    for i in plans:
        plans_string = list(map(int,i.split(' ')))
        data.append(plans_string[0])
        dictplans[idx] += plans_string[1:]
        if idx < len(plans)-1:
            dictplans[idx+1] = [num for num in dictplans[idx]]
        idx += 1
        
    arr = [0 for _ in range(len(clients))]
    
    for i in clients:
        clients_string = list(map(int,i.split(' ')))
        idx = bisect_left(data, clients_string[0])
        if idx >= len(plans):
            continue
        for j in range(idx, len(plans)):
            if set(dictplans[j]) >= set(clients_string[1:]):
                arr[clients.index(i)] = j+1
                break
    return arr
    
    
print(solution(5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"])) #=> [3,3,1,0]
print(solution(4, ["38 2 3", "394 1 4"], ["10 2 3", "300 1 2 3 4", "500 1"])) #=> [1,2,0]

