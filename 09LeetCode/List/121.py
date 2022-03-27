#주식을 사고 파는 가장 좋은 시점
#한번의 거래로 낼 수 있는 최대 이익
#[7,1,5,3,6,4] -> 5
#1일 때 사서 6일 때 팔면 5의 이익을 얻음
import sys
def stock(arr = [7,1,5,3,6,4]):
    #저점에 사서 고점에 팔아야함
    mintime = sys.maxsize
    maxprofit = -sys.maxsize
    for time in arr:
        mintime = min(mintime, time) #->이동하면서 min갱신
        maxprofit = max(maxprofit, time - mintime) #->이동하면서 max갱신
        
    return maxprofit
print(stock())