#Best Time to Buy And Sell Stock 2
#121(List)와 다르게 여러 번 사고 팔 수 있음
def maxProfit(self, prices):
    result = 0
    #값이 오르는 경우 매번 그리디 계산
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            result += prices[i+1] - prices[i]
    return result

def maxProfit(self, prices):
    #0보다 크면 무조건 합산
    return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices-1)))