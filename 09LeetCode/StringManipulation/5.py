#가장 긴 팰린드롬 부분 문자열
#입력 : "babad"
#출력 : "bab" 또는 "aba"
#입력 : "cbbd"
#출력 : "bb"
def longest(input):
    def expand(left, right): #주어진 위치로부터 left, right가 같으면 양옆으로 넓혀나감
        while left >= 0 and right < len(input) and input[left] == input[right]:
            left -= 1
            right += 1
        return input[left+1:right] #while문을 만족하는 범위의 부분문자열
        #while문 거친 후, 더 이상 left위치, right위치의 값이 같지 않음 -> 직전 left, right 범위 s리턴
        #while문 거치지 않으면 self.expand(s,i,i+2)를 리턴함. s[i+1:i+2] = s[i+1]문자 1개
        
    if len(input) < 2 or input == input[::-1]: #거꾸로해도 같은 문자열일 때(전체가 팰린드롬일 때)
        return input
    
    result = ''
    for i in range(len(input) - 1): #(i, i+1)은 짝수 개인 경우, (i, i+2)는 홀수 개인 경우!
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    
    return result

print(longest("babad"))