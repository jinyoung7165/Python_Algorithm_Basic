#Remove k digits
#k개의 수를 없앴을 때 얻는 가장 작은 수 구하라
#1432219, k=3 -> 1219
#10200, k=1 -> 200 (0200자동으로 200됨)
#10, k=2 -> 0
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #k개를 지움
        #앞자리 수가 뒷자리수보다 크면 지우는 게 좋음
        #지운 수들 다음이 0이면 최소
        if k >= len(num):
            return '0'
        stack = []
        for n in num:
            while stack and k and stack[-1] > int(n): #앞자리가 뒷자리보다 클 때
                k -= 1
                stack.pop()
            stack.append(int(n))
            
        while k and stack:
            k -= 1
            stack.pop()
            
        while stack and stack[0] == 0 and len(stack) > 1:
            stack.pop(0)
            
        return ''.join(map(str, stack))
