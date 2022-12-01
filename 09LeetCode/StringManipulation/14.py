#Longest Common Prefix
#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Input: strs = ["dog","racecar","car"]
#Output: ""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        strs.sort(key = lambda x: len(x))
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]