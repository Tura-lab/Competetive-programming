class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        dp = [0]*len(s)
        ans = 0
        
        for i in range(len(s)):
            if s[i] == ')' and i>0:
                if s[i-1]=='(':
                    dp[i] = 2
                    if i-2>=0:
                        dp[i] += dp[i-2]

                
                elif s[i-1]==')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = 2 + dp[i-1] 
                    if i-dp[i-1]-2 >=0:
                        dp[i] += dp[i-dp[i-1]-2]
            
            ans = max(ans, dp[i])
            
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack = []
#         found = set()

#         for i in range(len(s)):
            
#             if s[i] == '(':
#                 stack.append(i)
            
#             else:
#                 if stack:
#                     j = stack.pop()
#                     found.add((j,i))
#                     if (j+1, i-1) in found:
#                         found.remove((j+1, i-1))
        
#         new = []
#         ans = 0
#         found = sorted(list(found), key = lambda x: x[0])
#         for i,j in found:
#             if not new:
#                 new.append([i,j])
#             elif new[-1][1] +1== i:
#                 new[-1][1] = j
#             elif new[-1][1] +1 > i:
#                 if j-i > new[-1][1]-new[-1][0]:
#                     new.pop()
#                     new.append([i,j])                    
#             else:
#                 new.append([i,j])
            
#             ans = max(ans, new[-1][1] - new[-1][0] +1)
                
#         # print(found)
#         return ans