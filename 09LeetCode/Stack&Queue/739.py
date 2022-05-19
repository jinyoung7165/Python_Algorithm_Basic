#Daily Temperatures
#매일의 화씨온도 리스트를 받아 더 따뜻한 날을 위해선 며칠을 기다려야하는지 출력
#[73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
def dailyTemperatures(T = [73,74,75,71,69,72,76,73]):
    answer = [0] * len(T)
    stack = [] #자신보다 높은 다음 온도를 기다리는 애들의 인덱스. 자신보다 높은 애가 오면 빠지고, 낮은 애가 오면 계속 쌓임
    for i, cur in enumerate(T):
        #현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i -last #자신과의 인덱스 차이
        stack.append(i) #인덱스를 넣음
    
    return answer