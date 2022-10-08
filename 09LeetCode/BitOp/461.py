#두 정수 몇 비트가 다른지
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')