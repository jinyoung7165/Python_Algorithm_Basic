#셔틀버스
#셔틀은 09:00부터 총 n회, t분 간격으로 도착, 한 번에 최대 m명 탑승 가능
#도착한 순간 대기열까지 포함해 순서대로 태움(09:00에 대기한 사람도 자리 있으면 09:00에 탈 수 있음)
#어떤 멤버가 몇 시에 도착하는지 알아냄
#셔틀을 타고 사무실 도착할 시간 중 가장 늦은 시각 구하라
#나는 같은 시각에 도착한 크루 중 가장 뒤에 섬
#모든 크루는 23:59에 대기열에서 없어짐
def solution(n, t, m, timetable): #셔틀 운행수, 간격, 최대 탑승 크루 수, 대기열 도착시간 배열("hh:mm")
    timetable = [int(time[:2]) * 60 + int(time[3:]) 
                 for time in timetable] #분으로 표시
    timetable.sort()
    current = 540
    for _ in range(n):
        for _ in range(m):
            #대기 있는 경우 나는 1분 전 도착
            if timetable and timetable[0] <= current:
                candidate = timetable.pop(0) - 1
            else: #대기 없는 경우 정시 도착
                candidate = current
        current += t
    #시,분으로 다시 변경
    h, m = divmod(candidate, 60)
    return str(h).zfill(2) + ":" + str(m).zfill(2) #두 자릿수 안되는 경우 왼쪽에 0 삽입
            
print(solution(1,1,5,["08:00","08:01","08:02","08:03"])) #"09:00"
print(solution(2,10,2,["09:10","09:09","08:00"])) #09:09
print(solution(2,1,2,["09:00","09:00","09:00","09:00"])) #08:59
print(solution(1,1,5,["00:01","00:01","00:01","00:01","00:01",])) #00:00
print(solution(1,1,1,["23:59"])) #09:00
print(solution(10,60,45,["23:59","23:59","23:59","23:59","23:59","23:59",
                         "23:59","23:59","23:59","23:59","23:59","23:59",
                         "23:59","23:59","23:59","23:59",])) #18:00