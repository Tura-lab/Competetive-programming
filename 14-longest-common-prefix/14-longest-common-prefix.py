class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        item = strs[0]
        for word in strs:
            if len(word)<len(item):
                item = word
        for i in range(len(item)):
            val = item[i]
            for j in range(0,len(strs)):
                if strs[j][i] != val:
                    return ans
            ans += val
        return ans
                