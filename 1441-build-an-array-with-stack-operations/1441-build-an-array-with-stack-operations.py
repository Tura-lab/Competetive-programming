class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack =  []
        ans = []
        i = 0
        cur = 1
        count = 0
        while i < len(target):
            if cur == target[i]:
                while stack and count:
                    ans.append("Pop")
                    stack.pop()
                    count -= 1
                ans.append("Push")
                stack.append(cur)
                cur += 1
                i += 1
            else:
                stack.append(cur)
                ans.append("Push")
                count += 1
                cur += 1
                
        return ans