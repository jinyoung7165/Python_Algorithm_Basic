#Minimun Window Substring
import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, char in enumerate(s, 1):
            missing -= need[char] > 0 #missing: need에 존재하지 않으면 0(False), 존재하면 1(True)을 뺌
            need[char] -= 1 #need는 아무튼 감소시킴(T충족시 0, T에 없거나 과하면 음수)

            #필요 문자 모두 찾았으면 왼쪽 포인터 이동하며 윈도우 사이즈 줄이자
            if missing == 0:
                while left < right and need[s[left]] < 0: #need=0 :T에 속하는 원소인데 과하지 않을 때까지
                    need[s[left]] += 1 #필요 없거나 과한 원소 need 감소한 것 채우고, window에선 빼자
                    left += 1
                if not end or right-left <= end-start: #사이즈 작아지면 갱신
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
        return s[start:end]