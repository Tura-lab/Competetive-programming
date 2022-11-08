class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        minutes = {4:32, 5:16, 6:8, 7:4, 8:2, 9:1}
        hours = {0:8, 1:4, 2:2, 3:1}
        
        nums = list(range(10))
        
        ans = []
        path = []
        def dfs(i):
            if len(path) > turnedOn:
                return
            if i == 10:
                if len(path) != turnedOn:
                    return
                minute = 0
                hour = 0
                for num in path:
                    if num > 3:
                        minute += minutes[num]
                    else:
                        hour += hours[num]
                
                h = str(hour)
                m = '0'*(2-len(str(minute))) + str(minute)
                if 0<=int(h)<=11 and 0<=int(m)<=59:
                    ans.append(str(hour) + ':' + '0'*(2-len(str(minute))) + str(minute))
                return
            
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            dfs(i+1)
        
        dfs(0)
        return ans
            