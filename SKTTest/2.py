#연간 납부=이번달 포함 12개월 동안의 납부 총합
#다음달부터 VIP고객, 다음달엔 VIP가 아니게 되는 고객의 수를 return
#n=고객 수
#periods[i]=i+1번 고객의 가입기간(n)
#estimates[i]=i+1번 고객의 담달예정금액(n)
#payments=고객 납부내역 2차원 배열(n*12)
#payments[i][j]=i+1번 고객의 11-j달 전에 납부한 금액
#payments[i][11]=i+1번 고객의 이번 달 납부 금액
'''
가입기간이 24개월 미만인 고객은 VIP못 됨
다음달 24개월이면 최근 12개월 납부금액 900000 충족 시 vip :24개월 이상~120개월 미만
120개월 이상: 최근 12개월 납부금액 600000 충족 시 vip
'''
#1. period 24개월 미만 -> pass
#2. period 24~60 -> payments
#3. period 60~ -> payments
#4. period+1 -> estimates봄
def solution(periods, payments, estimates):
    result = [0, 0]
    n = len(periods) #사람 수
    for i in range(n):
        sum_pay = sum(payments[i])
        next_sum_pay = sum_pay + estimates[i] - payments[i][0]
        if 24 <= periods[i]: #현재도 VIP가능
            if periods[i] < 60: #5년 미만 고객
                if 59 == periods[i]:
                    if sum_pay < 900000 and next_sum_pay >= 600000: #다음달부터 VIP
                        result[0] += 1
                    elif sum_pay >= 900000 and next_sum_pay < 600000: #다음달부터 VIP 아님
                        result[1] += 1
                    
                else:
                    if sum_pay < 900000 and next_sum_pay >= 900000: #다음달부터 VIP
                        result[0] += 1
                    elif sum_pay >= 900000 and next_sum_pay < 900000: #다음달부터 VIP 아님
                        result[1] += 1
                    
            else: #현재 5년 이상 고객
                if sum_pay >= 600000 and next_sum_pay < 600000: #다음달부터 VIP 아님
                    result[1] += 1
                elif sum_pay < 600000 and next_sum_pay >= 600000: #다음달부터 VIP
                    result[0] += 1
                    
        elif 23 == periods[i]: #estimates봄
            if next_sum_pay >= 900000: #다음달부터 VIP
                result[0] += 1
    return result
           
print(solution([20,23,24], [[100000 for _ in range(12)], [100000 for _ in range(12)], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]], [100000, 100000, 100000])) #(2번),(3번) => [1,1]