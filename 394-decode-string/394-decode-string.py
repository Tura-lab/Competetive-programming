class Solution:
    def decodeString(self , s, k=1, i=0): 
        out = ''
        l=''
        j=i
        while j<len(s):
            if s[j].isalpha():
                out += s[j]
            elif s[j].isdigit():
                if j-1>-1 and s[j-1].isdigit():
                    l+=s[j]
                else:
                    l=s[j]
            elif s[j] == '[':
                added, num = self.decodeString(s, int(l), j+1)
                out += added
                j=num
            else:
                return out * k, j
            j+=1
        return out
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         stack = []
#         for i in range(len(s)):
#             if s[i] != ']':
#                 if s[i] in '1234567890':
#                     if stack and stack[-1][-1] in '1234567890':
#                         stack[-1] += s[i]
#                     else:
#                         stack.append(s[i])
#                 else:
#                     stack.append(s[i])
            
#             else:
#                 j=len(stack)-1
#                 while j>-1 and stack[j] != '[':
#                     j-=1
#                 stack[j-1:] = (stack[j+1:]) * int(stack[j-1])
#         return ''.join(stack)
