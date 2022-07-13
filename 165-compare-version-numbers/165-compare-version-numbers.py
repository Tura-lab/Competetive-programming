class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v2 = [int(i) for i in version2.split('.')]
        v1 = [int(i) for i in version1.split('.')]
        
        for i in range(max(len(v1), len(v2))):
            if (0 if i>=len(v1) else v1[i]) < (0 if i>=len(v2) else v2[i]):
                return -1
            elif(0 if i>=len(v2) else v2[i]) < (0 if i>=len(v1) else v1[i]):
                return 1
        
        return 0