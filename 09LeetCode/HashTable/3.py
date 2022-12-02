#Long "Substring" Without Repeating Characters
#중복 문자가 없는 가장 긴 부분문자열의 길이 리턴
#"abcabcbb" => 3("abc")
#"bbb" => 1
#"pwwkew" => 3("wkew") !주의: pwkew는 Subsequence(부분수열)이다
#슬라이딩 윈도우로 한 칸씩 이동하면서 윈도우 내에 문자 중복이 없도록 투 포인터로 윈도우 사이즈를 조정(bs왜 안써-> for문 한 번만 쭉 돌리며 start의 범위만 본다)
def lengthOfLongestSubstring(s = "abcabcbb"):
    #원소 반복 없이 가장 긴 부분문자열
    #현재 원소가 갱신된 시작 이후로 ~ 여태 지나쳐온 애들 중에 있는지 확인해야함
    past = {}
    max_len = 0
    temp = 0 #시작 위치
    for i, c in enumerate(s):
        if c in past and past[c]>=temp: #이미 지나쳐 옴. 중복된 원소의 시작 위치 갱신
            temp = past[c] + 1
        max_len = max(max_len, i-temp+1)
        past[c] = i
    return max_len