#Remove k digits
#연속된 k개의 수를 없앴을 때 얻는 가장 작은 수 구하라
#1432219, k=3 -> 1219
#10200, k=1 -> 200 (0200자동으로 200됨)
#10, k=2 -> 0
def removeKdigits(self, num: str, k: int) -> str:
    size = len(num)
    if size == k: return '0'
    stack = []
    for n in num:
        while stack and k and stack[-1] > int(n):
            stack.pop()
            k -= 1
        if len(stack) == 1 and stack[-1] == 0:# not leading 0
            stack.pop()
        stack.append(int(n))
    while k:
        stack.pop()
        k -= 1
    return ''.join(map(str,stack))  