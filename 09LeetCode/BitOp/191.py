#부호없는 정수형을 입력받아 1비트의 개수 출력하라
def hammingWeight(self, n: int) -> int:
    return bin(n).count('1')

def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        #N에서 1을 뺀 값과 N AND연산 -> 1의 개수 1개씩 빠짐-> 횟수 측정
        n &= n - 1
        count += 1
    return count 