#전화번호 문자 조합
#2-9의 숫자 주어졌을 때 전화번호 키패드로 조합가능한 모든 문자열을 출력하라
#2:abc 3:def 4:ghi 5:jkl 6:mno 7:pqrs 8:tuv 9:wxyz
#"23" => ["ad""ae""af""bd""be""bf""cd""ce""cf"]
#2는 abc 3은 def가 가능하므로 9가지의 경우가 나온다
#전체를 탐색해야 풀 수 있다. 가능한 경우를 모두 조합해 전체를 탐색한 후 백트래킹
digits = "23"
dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
path = "" #지금까지의 탐색 경로(문자열)
result = []

def dfs(idx, path):
    if  len(path) == len(digits): #숫자의 개수만큼 탐색했을 때
        result.append(path)
        return
    
    for i in range(idx, len(digits)): #각 자리의 숫자마다 반복
        for j in dic[digits[i]]: #숫자에 해당하는 문자들에 대해 반복
            dfs(i+1, path+j) #다음 자리의 수 볼 때 현재 자리까지의 문자열 넘김

def main():
    if not digits: return [] #예외처리
    dfs(0, "") #첫번째 자리부터
    return result

print(main())
            