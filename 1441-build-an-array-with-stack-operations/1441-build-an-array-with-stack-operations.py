class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 0
        cur = 1
        count = 0
        while i < len(target):
            if cur == target[i]:
                while count:
                    ans.append("Pop")
                    count -= 1
                ans.append("Push")
                cur += 1
                i += 1
            else:
                ans.append("Push")
                count += 1
                cur += 1
                
        return ans