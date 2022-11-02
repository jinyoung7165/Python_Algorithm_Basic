#Longest Repeating Character Replacement
#s = "AAABBC", k=2 -> 5 B를 두 번 A로 바꾸면 A연속5번 나옴
import collections


def charReplacement(self, s, k):
    left = right = 0
    counts = collections.Counter()
    for right in range(1, len(s)+1):
        counts[s[right-1]] += 1
        max_char_n = counts.most_common(1)[0][1]
        
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    return right - left
