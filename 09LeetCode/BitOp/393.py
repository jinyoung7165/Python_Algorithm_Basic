#UTF-8검증
class Solution:
    def validUtf8(self, data: List[int]) -> bool: 
        def check(size):
            for i in range(start + 1, start + size +1):
                if i >= len(data) or (data[i] >> 6) != 0b10: #10으로 시작
                    return False
            return True
        
        start = 0
        while start < len(data): #여러 문자일 수 있음
            #첫 바이트 기준 총 문자 바이트 판별
            first = data[start]
            print(first, start)
            if (first >> 3) == 0b11110 and check(3): #4바이트 -> 나머지 3바이트 확인
                start += 4
            elif (first >> 4) == 0b1110 and check(2): #3바이트
                start += 3
            elif (first >> 5) == 0b110 and check(1): #2바이트
                start += 2
            elif (first >> 7) == 0: #1바이트
                start += 1
            else:
                return False
        return True