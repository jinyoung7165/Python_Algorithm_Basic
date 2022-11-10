#다트 게임
#다트 세 차례 던짐 -> 점수 합계. 각 점수 0-10. s, d(점수^2), t(점수^3) 영역 존재
# (*)당첨 시 해당 점수, 직전 점수를 각 2배
# (#)당첨 시 해당 점수 마이너스
# 위의 당첨들은 중첩 가능. S/D/T뒤에 옴
#총점수 반환해라
#문자열 처리
def solution(dartResult):
    score = []
    n = ''  #두 자릿수일 경우 대비해 이전 숫자 저장
    for i in dartResult:
        if i.isdigit():
            n += i
        elif i == 'S':
            score.append(int(n) ** 1)
            n = ''
        elif i == 'D':
            score.append(int(n) ** 2)
            n = ''
        elif i == 'T':
            score.append(int(n) ** 3)
            n = ''
        elif i == '*':
            last = score.pop()
            if len(score) > 0:
                score.append((score.pop())*2)
            score.append(last*2)
        elif i == '#':
            score.append((score.pop())*-1)
    return sum(score)

'''     
def solution(dartResult):
    nums = [0]
    
    for s in dartResult:
        if s == 'S':
            nums.append(0) #연산자 표시
        elif s == 'D':
            nums[-1] **= 2 #해당 값 제곱
            nums.append(0)
        elif s == 'T':
            nums[-1] **= 3
            nums.append(0)
        elif s == '*':
            nums[-2] *= 2 #이전 값 두 배
            if len(nums) > 2:
                nums[-3] *= 2 #그 이전 값 두 배
        elif s == '#':
            nums[-2] *= -1 #이전 값 -1배
        else: 
        #자릿수 올림 -> 연산자의 경우 0-> 10곱해도 노상관
            nums[-1] = nums[-1]*10 + int(s)
    return sum(nums) #연산자 0-> 더해도 0
'''
print(solution("1S2D*3T")) #37
print(solution("1D2S#10S")) #9
print(solution("1D2S0T")) #3
print(solution("1S*2T*3S")) #23
print(solution("1D#2S*3S")) #5
print(solution("1T2D3D#")) #-4
print(solution("1D2S3T*")) #59