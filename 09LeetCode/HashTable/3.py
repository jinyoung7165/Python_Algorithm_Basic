#Long "Substring" Without Repeating Characters
#중복 문자가 없는 가장 긴 부분문자열의 길이 리턴
#"abcabcbb" => 3("abc")
#"bbb" => 1
#"pwwkew" => 3("wkew") !주의: pwkew는 Subsequence(부분수열)이다
#슬라이딩 윈도우로 한 칸씩 이동하면서 윈도우 내에 문자 중복이 없도록 투 포인터로 윈도우 사이즈를 조정(bs왜 안써-> for문 한 번만 쭉 돌리며 start의 범위만 본다)
def lengthOfLongestSubstring(s = "abcabcbb"):
    used = {} #윈도우 내 이미 나온 문자들의 인덱스
    max_length = start = 0
    for index, char in enumerate(s):
        #이미 전에 등장했던 문자면 "start" 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1 #이전에 char이 나온 위치 다음부터 윈도우 시작
        else: #최대 부분 문자열의 길이 갱신
            max_length += max(max_length, index - start + 1)
        
        used[char] = index #사용한 문자의 위치 삽입
        
    return max_length