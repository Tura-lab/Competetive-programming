class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
#         i = len(v1)-1
#         while i>0 and v1[i] == '0':
#             i-=1
#         v1 = v1[:i+1]
        
#         i = len(v2)-1
#         while i>0 and v2 and v2[i] == '0':
#             i-=1
#         v2 = v2[:i+1]
        
        
        v2 = [int(i) for i in v2]
        v1 = [int(i) for i in v1]
        
        for i in range(max(len(v1), len(v2))):
            if (0 if i>=len(v1) else v1[i]) < (0 if i>=len(v2) else v2[i]):
                return -1
            elif(0 if i>=len(v2) else v2[i]) < (0 if i>=len(v1) else v1[i]):
                return 1
        
        return 0