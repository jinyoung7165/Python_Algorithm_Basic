#백준 2878 - 캔디캔디
#사탕 m개 -> n명에게 분배. 각 사람의 요구에 비해 못 받는 개수의 제곱의 합을 최소로
#요구의 합-m =부족한 양 -> 각 사람에게 분배해서 제곱의 합 최소화
#최대한 부족한 양을 골고루 분배
import sys
input = sys.stdin.readline
lst = []
M, N = map(int,input().split())
for i in range(N):
    lst.append(int(input()))
lst.sort()  #요구량이 작은 사람 먼저 분배
give_me_a_candies = sum(lst) - M # 필요 캔디 - 가진 캔디 = 부족 캔디
ans = 0

for i in range(N): #사람 별로 반복(가장 요구 작은 사람부터)
    # 분노가 최소인 지점 => 각 사람들이 못 받은 캔디 개수가 같을 때
    # vacant는 분노가 최소가 되게 하는 한 사람이 못 받은 캔디의 개수
    vacant = give_me_a_candies // ( N - i ) #남은 사람들 수만큼 골고루 부족 분배

    if lst[i] >= vacant: #요구량이 부족한 양보다 많으면
        given = vacant #부족한 양 골고루 나눠줌
        ans += given**2 #총 나눠준 사탕 수 누적
    else:     # 필요로 한 사탕 개수가 vacant보다 작다면 요구량만큼만 줌
        given = lst[i]
        ans += given**2
    give_me_a_candies -= given #남은 사탕 계산

print(ans%(2**64))

                    
            
    
    
