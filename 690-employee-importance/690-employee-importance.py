"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        imps = {item.id:[item.importance, item.subordinates] for item in employees}
        
        ans = [0]
        
        ans[0] += imps[id][0]
        subs = imps[id][1]
        
        def subAdder(subs):
            for sub in subs:
                ans[0] += imps[sub][0]
                subAdder(imps[sub][1])
        
        subAdder(subs)
        return ans[0]