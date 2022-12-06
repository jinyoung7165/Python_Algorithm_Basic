#전화번호 문자 조합 #Letter Combinations of a Phone Number
#2-9의 숫자 주어졌을 때 전화번호 키패드로 조합가능한 모든 문자열을 출력하라
#2:abc 3:def 4:ghi 5:jkl 6:mno 7:pqrs 8:tuv 9:wxyz
#"23" => ["ad""ae""af""bd""be""bf""cd""ce""cf"]
#2는 abc 3은 def가 가능하므로 9가지의 경우가 나온다
#전체를 탐색해야 풀 수 있다. 가능한 경우를 모두 조합해 전체를 탐색한 후 백트래킹
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
        }
        result = []
        
        def comb(idx, path = ''): #path: 여태까지 탐색 경로
            if len(path) == len(digits): #원하는 개수만큼 찾음
                if digits: #not digits면 result = []
                    result.append(path) #여태까지의 탐색 경로 넣음
                return
            for i in dic[digits[idx]]: #해당 수에 대한 알파벳들
                comb(idx+1, path+i) #다음 수 볼 것, 현재까지의 경로
        comb(0)
        return result