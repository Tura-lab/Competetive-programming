class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        d={}
        for i in range(len(temperatures)):
            while stack and stack[-1][0]<temperatures[i]:
                temp = stack.pop()
                d[temp[1]] = i-temp[1]
            stack.append((temperatures[i],i))
        for temp in stack:
            d[temp[1]] =0
        return [d[n] for n in range(len(temperatures))]
